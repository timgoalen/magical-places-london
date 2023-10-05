from django import forms
from .models import Place, Comment


class AddPlaceForm(forms.ModelForm):
    place_name = forms.CharField(
        # Add HTML element ID values
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
    photo_url = forms.URLField(
        widget=forms.HiddenInput(attrs={"id": "photoUrl-field"}),
        label="Photo URL",
    )

    class Meta:
        model = Place
        fields = ["place_name", "latitude", "longitude", "address", "photo_url"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)

    comment = forms.CharField(widget=forms.Textarea, label="Add a Comment")
