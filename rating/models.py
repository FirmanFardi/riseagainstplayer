from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.


class Rating(models.Model):
    name = models.IntegerField(null=True, blank=True)

    def __integer__(self):
        return self.name