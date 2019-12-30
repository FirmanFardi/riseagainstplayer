from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name