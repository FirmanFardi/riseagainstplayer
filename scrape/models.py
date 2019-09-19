from django.db import models
from django.conf import settings
# Create your models here.

class Scraper(models.Model):
    title1=models.CharField(max_length=120)
    image1=models.ImageField(default="", editable=False)


    def __str__(self):
        return self.title1

