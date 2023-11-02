from django import forms
from .models import Place, Comment


class AddPlaceForm(forms.ModelForm):
    """
    FORM: Add Place.
    """
    # Add HTML element ID values.
    place_name = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "name-field"}),
        label="Place Name",
    )
    latitude = forms.FloatField(
        widget=forms.HiddenInput(attrs={"id": "latitude-field"}),
        label="Latitude",
    )
    longitude = forms.FloatField(
        widget=forms.HiddenInput(attrs={"id": "longitude-field"}),
        label="Longitude",
    )
    address = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "address-field"}),
        label="Address",
    )
    google_place_id = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "google-place-id-field"}),
        label="Google Place ID",
    )

    class Meta:
        model = Place
        fields = [
            "place_name", "latitude", "longitude", "address", "google_place_id"
            ]


class CommentForm(forms.ModelForm):
    """
    FORM: Add Comment.
    """

    class Meta:
        model = Comment
        fields = [
            "comment",
        ]

    comment = forms.CharField(widget=forms.Textarea, label="Add a Comment")
