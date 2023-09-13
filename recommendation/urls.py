from django.conf.urls import url

from . import views

app_name = 'recommendation'

urlpatterns = [
    url(r"^$", views.generate_recommendation, name="all"),
    url(r"^popular/$", views.popular_restaurant, name="popular"),
    
]