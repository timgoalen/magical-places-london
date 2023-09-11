from django.db import models
from django.urls import reverse


class Place(models.Model):
    place_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.place_name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    # check other 'on_delete' options
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.place_name
