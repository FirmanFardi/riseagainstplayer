from django.db import models
from django.conf import settings
from PIL import Image
from genre.models import Genre
from developer.models import Developer
from django.contrib.auth.models import User
from tag.models import Tag
# Create your models here.



class Steam(models.Model):
    gametitle=models.CharField(max_length=500)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField()
    tags = models.ManyToManyField(Tag,null=True)
    url=models.TextField()
    rating=models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['gametitle']


    def __str__(self):
        return self.gametitle
    

