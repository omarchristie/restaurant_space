from django.db import models
import datetime
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
import random

from faker import Faker
from ratings.models import Rating
from restaurant.models import Restaurant
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.utils import timeszone
#area [ 'New Kingston', 'Halfway Tree', 'Kingston', 'Liguanea', 'Spanish Town' , 'Ocho Rios', 'Montego Bay']
#type_restaurant ['Jamaican', 'Chinese', 'Mexican' ,'Indian', 'Japanese', 'American']
#type_ambiance[ 'Bar&Grill','Fine Dining', 'Family Friendly']
ratings = [1,2,3,4,5]
comment = ["\"the food was great\"", "\"The ambiance was beatiful\"", "\"Great Job\"", "\"I liked this restaurant\"", "\"Thumbs Up\"", "\"Okay\"", "\"Nice\"", "\"Service was excellent\"", "\"GOOD\"", "\"nice\"","\"OK\"", "\"Good portion\""]
description = ["\" The place to eat\"", "\" food king\"", "\"We are open\"", "\"We will to serve you\"", "\"The food place\"", "\"best in town\"", "\" happy tongue\"", "\"We make you smile\"", "\"happy dance\"", "\"it reminds me of home\"","\"experience the culture\"", "\"love\"", "\"visit us\""]

def create_post(N):
        fake = Faker()
        for _ in range(N):
                title =fake.name(),
                status = random.choice (['published', 'draft']),
                Post.objects.create(title= title+ "Post !!!",
                author = User.objects.get(id=id),
                slug="-".join(title.lower().split()),
                comment= comment[random.randint(0, len(comment)-1)],
                created = timezone.now(),
                updated= timezone.now(),
                )
create_post (10)
print ("Posts were successfully populated")

#def create_restaurant(N):
        #fake = Faker()
	#for _ in range(N):
        
                #ake.restaurant.name(),
                #ake.address(),
                #ake.restaurant.type(),
                #description[random.randint(0, len(description)-1)]
                #aker.image.food(); //returns "https://www.google.com/search?q=food+/640/480&source=lnms&tbm=isch&sa=X&ved=0ahUKEwifzdH8n6TiAhWwslkKHVCIDFkQ_AUIDigB&biw=1920&bih=969s"(),#/

#reate_restaurant (10)
#rint (" ADD TYPE OF RESTAURANT OT CODE restaurants were successfully populated")

#def create_profile
       #fake = Faker()
       #for _ in range (N):
            #   fake.simple_profile(sex= None)
        #   create_profile (10)
        #print ("Profiles were successfully populated")
                