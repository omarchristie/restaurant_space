from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Rating
from restaurant.models import Restaurant
from .forms import RatingForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def add_rating_to_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    current_user = request.user
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.restaurant = restaurant
            rating.user = current_user
            rating.save()
            return redirect('restaurant:single', pk=restaurant.pk)
    else:
        form = RatingForm()
    return render(request, 'ratings/rating_form.html', {'form': form})
    
#######################################
##  ##class based views ##
#######################################
    
    
class RatingListView(ListView, LoginRequiredMixin):
    model = Rating

    def get_queryset(self, request):
        current_user = request.user
        return Rating.objects.filter(user = current_user.username).order_by('-created_at')

class RatingDetailView(DetailView, LoginRequiredMixin):
    model = Rating