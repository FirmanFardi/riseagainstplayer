from django.db import models
from django.conf import settings
from PIL import Image
from genre.models import Genre
from developer.models import Developer
from rating.models import Rating
from django.contrib.auth.models import User
from tag.models import Tag
from constants import SORTED_RATING, SORTED_YEARS
# Create your models here.



class Steam(models.Model):
    gametitle=models.CharField(max_length=500,null=True,blank=True)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,default='default.jpg')
    tags = models.ManyToManyField(Tag,null=True)
    url=models.TextField()
    rating=models.IntegerField(null=True,blank=True)
    to_be_rated = models.NullBooleanField(null=True, default=False)

    class Meta:
        ordering = ['gametitle']


    def __str__(self):
        return str(self.gametitle)
    

class GameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Steam, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SORTED_RATING, blank=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.user, self.game, self.score)