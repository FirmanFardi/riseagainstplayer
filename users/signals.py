# save when user is created
from django.db.models.signals import post_save
# sender
from django.contrib.auth.models import User
# receiver
from django.dispatch import receiver
from .models import Profile

# post_save send a signal to receiver
# instance is the data created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
