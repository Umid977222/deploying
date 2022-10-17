from django.db import models


def upload_location(instance, filename):
    return filename


class Adds(models.Model):
    name = models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to=upload_location, default='posts/default.jpg')
    description = models.TextField()
    add_bot_button = models.BooleanField()
