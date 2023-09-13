from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from restaurant.models import Restaurant
from . import models
from .forms import RestaurantForm

class CreateRestaurant(LoginRequiredMixin, generic.CreateView):
    form_class = RestaurantForm
    template_name = "restaurant/restaurant_form.html"
    success_message = 'New Restaurant has been created'
    


class SingleRestaurant(LoginRequiredMixin, generic.DetailView):
    model = Restaurant

class ListRestaurant(LoginRequiredMixin, generic.ListView):
    model = Restaurant