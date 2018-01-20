from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	bio = models.TextField(max_length=500, blank=True)
	username = models.CharField(max_length=30, blank=False)
	first_name = models.CharField(max_length=30, blank=False)
	last_name = models.CharField(max_length=30, blank=False)
	email = models.EmailField(max_length=254, blank=False)
	grade = models.CharField(max_length=30, blank=False)
	major = models.CharField(max_length=30, blank=False)
	interest1 = models.CharField(max_length=30, blank=False)
	interest2 = models.CharField(max_length=30, blank=False)
	interest3 = models.CharField(max_length=30, blank=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    print('update_user_profile')
    if created:
        print('created')
        Profile.objects.create(user=instance)
    instance.profile.save()

    

