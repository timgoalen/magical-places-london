from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# 'PLACE' MODEL


class Place(models.Model):
    place_name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="places", default=1
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        # need this, if also doing in the view?..
        ordering = ["-created_on"]

    def __str__(self):
        return self.place_name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})


# 'COMMENT' MODEL


class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment} by {self.author}"

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})


# 'FAVOURITE' MODEL


class Favourite(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="favourites"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")
    favourited_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["place", "user"], name="unique_favourite")
        ]
