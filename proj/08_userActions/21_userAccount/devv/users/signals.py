from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User #django model
from .models import Profile

# @receiver(post_save, sender=Profile)    
def createProfile(sender, instance, created, **kwargs):
    print("profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
            )

def profileDeleted(sender, instance, **kwargs):
    print("profile signal triggered")
    user = instance.user
    user.delete()
    print("Deleting User")

post_save.connect(createProfile, sender=User)
post_delete.connect(profileDeleted, sender=Profile)