from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.place_name
