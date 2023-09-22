from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# 'PLACE' MODEL


class Place(models.Model):
    place_name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contributer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="places", default=1
    )
    updated_on = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(default=timezone.now)
    favourited = models.ManyToManyField(
        User, related_name="favourited_places", blank=True
    )

    class Meta:
        # need this, if also doing in the view?..
        ordering = ["-created_on"]

    def __str__(self):
        return self.place_name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})

    # using this?..
    def number_of_times_favourited(self):
        return self.favourited.count()


# 'COMMENT' MODEL


class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment} by {self.author}"

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})
