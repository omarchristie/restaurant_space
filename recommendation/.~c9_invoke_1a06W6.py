from django.db import models
from ratings.models import Rating
from math import sqrt
from accounts.models import UserProfile
from django.contrib.auth.models import User

def similarity_distance(user,other):
    
    similar = {}
    sum_check = 0
    otheruser_rest = Rating.objects.filter(user__username=other)
    user_rest = Rating.objects.filter(user__username=user)
    
    for user_rat  in user_rest:
        for other_rat in otheruser_rest:
            
            if other_rat.restaurant == user_rat.restaurant:
                similar[user_rat.restaurant]=1
    print("")
    print("similar")
    print(similar)
    
    if not similar:
        print("nothing similar")
        return 0
    
    for user_rat  in user_rest:
        for other_rat in otheruser_rest:
            if other_rat.restaurant == user_rat.restaurant:
                sum_check = sum_check + ((user_rat.res_rating - other_rat.res_rating)**2)
    result = (1/1+sqrt(sum_check))
    print("results:")
    print(result)
    return (result) 




def get_recommendation(user):
    
    sim=0
    total={}
    simsums={}
    ranks={}
    
    other_user = User.objects.all()
    print(other_user)
    
    for name in other_user:
        if name.username != user.username:
            sim=similarity_distance(user.username,name.username)
            print("sim:")
            print("sim")
            if sim > 0:
                otheruser_rest = Rating.objects.filter(name__username=name.username)
                user_rest = Rating.objects.filter(name__username=user.username)
                for other in otheruser_rest:
                    for user in user_rest:
                        if other.restaurant == user.restaurant:
                            pass
                    if other.restaurant not in total:
                        total[other.restaurant] = 0
                        total[other.restaurant] = total[other.restaurant] + (other.res_rating*sim)
                            
                    if other.restaurant not in simsums:
                        simsums[other.restaurant]=0
                    simsums[other.restaurant] += sim
                            
    for i in total:
        ranks[i]=(total[i]/simsums[i])
    ranks=sorted(ranks, key=ranks.__getitem__)
    print("ranks:")
    print(ranks)
    return ranks
                                
                            
            
        
            
