from django.test import TestCase
from .forms import AddPlaceForm, CommentForm


class TestAddPlaceForm(TestCase):

    def test_place_name_is_required(self):
        form = AddPlaceForm({"place_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("place_name", form.errors.keys())
        self.assertEqual(form.errors["place_name"][0], "This field is required.")

    def test_fields_are_explicit_in_place_form_meta_class(self):
        form = AddPlaceForm
        self.assertEqual(form.Meta.fields, [
            "place_name", "latitude", "longitude", "address", "google_place_id"])


class TestCommentForm(TestCase):

    def test_comment_is_required(self):
        form = CommentForm({"comment": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("comment", form.errors.keys())
        self.assertEqual(form.errors["comment"][0], "This field is required.")

    def test_fields_are_explicit_in_comment_form_meta_class(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ["comment"])
