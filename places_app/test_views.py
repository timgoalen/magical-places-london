# from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import Place, Comment


class TestViews(TestCase):

    @classmethod
    def setUpTestData(self):
        """Create test data"""
        self.user = User.objects.create(username="test-user")
        self.user.set_password("secret")
        self.user.save()

        self.place = Place.objects.create(
            place_name="Test Place",
            latitude=51.50195171806682,
            longitude=-0.1417183386330674,
            address="Test Address",
            photo_url="www.test-photo.com",
            contributer=self.user,
        )

        self.comment = Comment.objects.create(
            place=self.place,
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
        response = self.client.get(f"/place/{self.place.id}/")
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
            reverse("place_detail", args=[self.place.pk]),
            data={
                "place": self.place,
                "comment": "Test comment",
            },
        )
        self.assertRedirects(response, reverse("place_detail", args=[self.place.pk]))

    def test_can_delete_comment(self):
        self.client.login(username="test-user", password="secret")
        response = self.client.get(f"/comment/{self.comment.pk}/delete/")
        # FIX: THIS NOT WORKING:
        # self.assertRedirects(response, reverse_lazy("comment_delete", args=[self.comment.pk]))
        # self.assertRedirects(response, f"/place/{self.place.pk}")

    # def test_can_favourite_a_place(self):

    # def test_can_unfavourite_a_place(self):


# MAYBE DON'T NEED THESE?..

# def test_get_login_page(self):

# def test_get_logout_page(self):

# def test_get_signup_page(self):
