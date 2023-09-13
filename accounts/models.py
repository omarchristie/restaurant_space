from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    
    # gender choice:
    GENDER_CHOICE= (
        ('Male','Male'),
        ('Female','Female')
        )

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Add any additional attributes you want
    gender = models.CharField(max_length=10, choices= GENDER_CHOICE)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='accounts_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return "@{}".format(self.user.username)