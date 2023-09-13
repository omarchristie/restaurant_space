from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from restaurant.models import Restaurant
from .recomender_alg import get_recommendation
from ratings.models import Rating
from collections import defaultdict

# Create your views here
@login_required
def generate_recommendation(request):
    restaurant = []
    ratings= Rating.objects.all()
    
    nested_dict = lambda: defaultdict(nested_dict)
    matrix= nested_dict()
    
    for rating in ratings:
        print(rating)
        matrix[rating.user.username][rating.restaurant.name]=rating.res_rating
    print("matrix")
    print(matrix)
    
    for name in matrix:
        print (name)
        print(matrix[name])
        for j in matrix[name]:
            print(matrix[name][j])
            
    if 'ochrist' in matrix:
        print('true')
        
    
    current_user = request.user.username
    recommendation = get_recommendation(current_user, matrix)
    for rec in recommendation:
        print("rec:")
        print(rec)
        print("recommendation[rec]")
        print(recommendation.get(rec))
        if recommendation[rec] > 2.5:
            restaurant.append(Restaurant.objects.filter(name = rec))
    print("list below")
    print (restaurant)
    return render(request, 'recommendation/recommended_restaurant.html', {'recommendation': restaurant})
    
    
    
@login_required
def popular_restaurant(request):
    
    rest_avg = {}
    restaurantlist = []
    
    restaurants = Restaurant.objects.all()
    
    for restaurant in restaurants:
        ratings = Rating.objects.filter(restaurant__name = restaurant.name)
        num = 0
        sumnum = 0
        
        if ratings:
            for rating in ratings:
                print("rating.res_rating")
                print(rating.res_rating)
                sumnum += rating.res_rating
                num += 1
        print("sumnum:")
        print(sumnum)
        print("num:")
        print(num)
        if num == 0:
            rest_avg[restaurant] = 0
        else:
            rest_avg[restaurant] = sumnum/num
        print("rest_avg")
        print(rest_avg)
        
    for res in rest_avg:
        if rest_avg[res] > 3:
            restaurantlist.append(Restaurant.objects.filter(name = res))
    return render(request, 'recommendation/popular.html', {'recommendation': restaurantlist})
