from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Place(models.Model):
    place_name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # check use for 'related_name': (if needed)
    contributer = models.ForeignKey(User, on_delete=models.SET("deleted_user"), related_name="my_places")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    favourited = models.ManyToManyField(
        User, related_name="place_favourited", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.place_name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})

    def number_of_times_favourited(self):
        return self.favourited.count()


class Comment(models.Model):
    place_name = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment} by {self.author}"
