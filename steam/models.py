from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.

class Steam(models.Model):
    gametitle=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField()
    tag=models.CharField(max_length=120)
    url=models.TextField()


    def __str__(self):
        return self.gametitle

