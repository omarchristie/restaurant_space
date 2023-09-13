# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True, default='')
    restaurant_pic = models.ImageField(upload_to='restaurant_pics',blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("restaurant:single", kwargs={'pk':self.pk})


    class Meta:
        ordering = ["name"]
    
