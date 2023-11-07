from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Place, Comment, Favourite


class TestViews(TestCase):

    @classmethod
    def setUpTestData(self):
        """Create test data"""
        self.user = User.objects.create(username="test-user")
        self.user.set_password("secret")
        self.user.save()

        self.place1 = Place.objects.create(
            place_name="Test Place 1",
            latitude=51.50195171806682,
            longitude=-0.1417183386330674,
            address="Test Address 1",
            google_place_id="1",
            contributer=self.user,
        )

        self.place2 = Place.objects.create(
            place_name="Test Place 2",
            latitude=51.50295171806682,
            longitude=-0.1427183386330674,
            address="Test Address 2",
            google_place_id="2",
            contributer=self.user,
        )

        self.comment = Comment.objects.create(
            place=self.place1,
            comment="Test comment",
            author=self.user,
        )

    def test_get_map_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html", "base.html")

    def test_get_list_page(self):
        response = self.client.get("/list_view/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list_view.html", "base.html")

    def test_get_detail_page(self):
        response = self.client.get(f"/place/{self.place1.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "place_detail.html", "base.html")

    def test_get_add_place_page(self):
        self.client.login(username="test-user", password="secret")
        response = self.client.get("/place/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "place_add.html", "base.html")

    def test_get_comment_update_page(self):
        self.client.login(username="test-user", password="secret")
        response = self.client.get(reverse("comment_edit", args=[self.comment.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "comment_edit.html", "base.html")

    def test_get_comment_delete_page(self):
        self.client.login(username="test-user", password="secret")
        response = self.client.get(reverse("comment_delete", args=[self.comment.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "comment_delete.html", "base.html")

    def test_can_create_comment(self):
        self.client.login(username="test-user", password="secret")
        response = self.client.post(
            reverse("place_detail", args=[self.place1.pk]),
            data={
                "place": self.place1,
                "comment": "Test comment",
            },
        )
        self.assertRedirects(response, reverse("place_detail", args=[self.place1.pk]))

    def test_can_delete_comment(self):
        self.client.login(username="test-user", password="secret")
        comment_count_before = Comment.objects.count()
        response = self.client.post(f"/comment/{self.comment.pk}/delete/")
        comment_count_after = Comment.objects.count()
        self.assertEqual(comment_count_after, comment_count_before - 1)
        self.assertEqual(response.status_code, 302)

    def test_get_404_page(self):
        response = self.client.get("/a-page-that-doesn't-exist/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_can_favourite_a_place_logged_in(self):
        self.client.login(username="test-user", password="secret")
        response = self.client.post(reverse("favourite_a_place", args=[self.place1.pk]), data={"place_id": self.place1.id})
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(Favourite.objects.filter(place=self.place1, user=self.user).exists())

    def test_can_unfavourite_a_place_logged_in(self):
        self.client.login(username="test-user", password="secret")
        Favourite.objects.create(place=self.place1, user=self.user)
        response = self.client.post(reverse("favourite_a_place", args=[self.place1.pk]), data={"place_id": self.place1.id})
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertFalse(Favourite.objects.filter(place=self.place1, user=self.user).exists())

    def test_attempting_favouriting_a_place_not_logged_in(self):
        response = self.client.post(reverse("favourite_a_place", args=[self.place1.pk]), data={"place_id": self.place1.id})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/favourites/1")

    def test_user_favourites_list_logged_in(self):
        self.client.login(username="test-user", password="secret")
        Favourite.objects.create(place=self.place1, user=self.user)
        response = self.client.get('/list_view/')
        user_favourites = response.context['user_favourites']
        self.assertIn(self.place1, user_favourites)
        self.assertNotIn(self.place2, user_favourites)

    def test_user_favourites_list_logged_out(self):
        response = self.client.get('/list_view/')
        user_favourites = response.context['user_favourites']
        self.assertEqual(list(user_favourites), [])
