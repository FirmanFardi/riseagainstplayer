from django.db import models

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=64,null=True,blank=True)

    def __str__(self):
        return self.name