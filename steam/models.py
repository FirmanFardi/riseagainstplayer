from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.

class Steam(models.Model):
    gametitle=models.CharField(max_length=120)
    price=models.CharField(max_length=120)
    image=models.ImageField()
    tag=models.ImageField()
    url=models.TextField()


    def __str__(self):
        return self.gametitle

