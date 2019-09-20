from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.

class Scraper(models.Model):
    title1=models.CharField(max_length=120)
    image1=models.ImageField(upload_to='profile_pics')
    url1=models.TextField()


    def __str__(self):
        return self.title1

