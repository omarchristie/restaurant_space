from django.conf.urls import url

from . import views

app_name = 'restaurant'


urlpatterns = [
    url(r"^$", views.ListRestaurant.as_view(), name="all"),
    url(r"^new/$", views.CreateRestaurant.as_view(), name="create"),
    url(r'^restaurant/(?P<pk>\d+)$', views.SingleRestaurant.as_view(), name='single'),
    
]