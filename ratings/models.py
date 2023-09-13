from django.conf import settings
from django.urls import reverse
from django.db import models

from restaurant.models import  Restaurant

from django.contrib.auth import get_user_model
User = get_user_model()


class Rating(models.Model):
    
    
    # gender choice:
    RATING_CHOICE= (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
        )
    
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    res_rating = models.IntegerField(choices= RATING_CHOICE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    restaurant = models.ForeignKey(Restaurant, related_name="ratings",null=True, blank=True,on_delete=models.PROTECT)

    def __int__(self):
        return self.res_rating
        
    def get_absolute_url(self):
        return reverse("restaurant:all")

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message","res_rating"]
