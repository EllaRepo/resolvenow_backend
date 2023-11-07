from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    full_name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'full_name']


    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Inspector(User):
    region = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)

class Region(models.Model):
    name = models.CharField(max_length=20)

class CompTypes(models.Model):
    name = models.CharField(max_length=20)

class Complaint(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")
    compTitle = models.CharField(max_length=128)
    city = models.CharField(max_length=20)
    subCity = models.CharField(max_length=20)
    landmark = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    region = models.CharField(max_length=20)
    compType = models.CharField(max_length=20)
    compSev =models.CharField(max_length=20)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "_state" in new_dict:
            del new_dict["_state"]
        return new_dict
    