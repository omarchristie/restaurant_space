from django.conf.urls import url

from . import views

app_name = 'ratings'

urlpatterns = [
    url(r"^$", views.RatingListView.as_view(), name="all"),
    url(r'^restaurant/(?P<pk>\d+)/ratings/$', views.add_rating_to_restaurant, name="add_rating_to_restaurant"),
    url(r"^rating/(?P<pk>\d+)$",views.RatingDetailView.as_view(),name="rating_detail")
    ]