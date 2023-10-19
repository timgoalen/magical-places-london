from django.test import TestCase
from django.contrib.auth.models import User
from .models import Place, Comment


class TestModels(TestCase):

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

    def test_place_string_method_returns_name(self):
        self.assertEqual(self.place.__str__(), self.place.place_name)

    def test_comment_string_method_returns_correct_string(self):
        expected_string = f"Comment {self.comment.comment} by {self.comment.author}"
        self.assertEqual(self.comment.__str__(), expected_string)

# DO THIS AGAIN WHEN A 'FAVOURITE' HAS BEEN SET UP IN THE TESTING DATA:
    # def test_favourite_string_method_returns_correct_string(self):
    #     expected_string = f"{self.user.username} favourited {self.place.place_name}"
    #     self.assertEqual(self.favourite.__str__(), expected_string)

    def test_get_place_absolute_url(self):
        expected_url = f"/place/{self.place.pk}/"
        self.assertEqual(self.place.get_absolute_url(), expected_url)

    def test_get_comment_absolute_url(self):
        expected_url = f"/place/{self.comment.place.pk}/"
        self.assertEqual(self.comment.get_absolute_url(), expected_url)
