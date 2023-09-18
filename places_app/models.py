from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Place(models.Model):
    place_name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contributer = models.ForeignKey(User, on_delete=models.SET("deleted_user"))
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
    # check other 'on_delete' options
    place_name = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.comment
