from django.db import models
from django.contrib.auth.models import User
from traitlets import default
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to = 'profile_pictures')
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile...'


    # the code below is called a signal, it automatically creates a new Profile whenever a new user have been registered in the database
    @receiver(post_save, sender = User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

