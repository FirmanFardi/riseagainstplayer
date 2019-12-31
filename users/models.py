from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
# cascade if user delete profile also delete posts , but not otherwise

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    favorite_tags = models.ManyToManyField('tag.Tag', blank=True)#no need to import, can import thorugh here
    favorite_genre = models.ForeignKey('genre.Genre', blank=True, null=True, on_delete=None)
    favorite_developer = models.ForeignKey('developer.Developer', blank=True, null=True, on_delete=None)


    def __str__(self):
        return f'{self.user.username} Profile'

    #it runs when the profile is save, if we upload image size>300 then image will resize to 
    #300 so that it will load faster and save alot of storage
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
