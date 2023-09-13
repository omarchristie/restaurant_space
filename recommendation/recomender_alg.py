from django.db import models
from ratings.models import Rating
from math import sqrt
from accounts.models import UserProfile
from django.contrib.auth.models import User

def similarity_distance(matrix, user, other):
    
    similar = {}
    sum_check = 0
    
    for restaurant  in matrix[user]:
        if restaurant in matrix[other]:
            print("restaurant")
            similar[restaurant]=1
                
    print("similar:")
    print(similar)
    
    if not similar:
        print("nothing similar")
        return 0
    
    for restaurant  in matrix[user]:
        if restaurant in matrix[other]:
            sum_check = sum_check + ((matrix[user][restaurant] - matrix[other][restaurant])**2)
    result = (1/1+sqrt(sum_check))
    print("results:")
    print(result)
    return (result) 




def get_recommendation(user, matrix):
    
    sim=0
    total={}
    simsums={}
    ranks={}
    
    for name in list(matrix):
        print("name")
        print(name)
        print("user")
        print(user)
        if name != user:
            sim=similarity_distance(matrix, user, name)
            print("sim:")
            print(sim)
            if sim > 0:
                for restaurant in matrix[name]:
                    print("name restaurant")
                    print(restaurant)
                    if restaurant not in matrix[user]:
                        print("not in user restaurant")
                        print(restaurant)
                        if restaurant not in total:
                            total[restaurant] = 0
                            print("total")
                            print (total)
                        total[restaurant] = total[restaurant] + (matrix[name][restaurant]*sim)
                        if restaurant not in simsums:
                            simsums[restaurant]=0
                            simsums[restaurant] += sim
                            print("simsums:")
                            print(simsums)
                    else:
                        print("user restaurant")
                        print(restaurant)
                        pass
                            
                            
    for i in total:
        ranks[i]= total[i]/simsums[i]
        print("ranks[i]:")
        print(ranks[i])
        
    
    print("ranks:")
    print(ranks)
    return ranks
                                
                            
            
        
            
