from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import UserProfile
 
from .forms import CreateUserForm
 
class CreateUserView(CreateView):
    success_url = reverse_lazy("login")
    form_class = CreateUserForm
    template_name = "accounts/signup.html"
    success_message = 'New user profile has been created'
 
    def form_valid(self, form):
        c = {'form': form, }
        user = form.save(commit=False)
        # Cleaned(normalized) data
        gender = form.cleaned_data['gender']
        profile_pic = form.cleaned_data['profile_pic']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()
 
        # Create UserProfile model
        UserProfile.objects.create(user=user, gender=gender, profile_pic=profile_pic)
 
        return super(CreateUserView, self).form_valid(form)
