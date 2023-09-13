from django import forms
from django.contrib.auth.models import User
 
class CreateUserForm(forms.ModelForm):
    # gender choice:
    GENDER_CHOICE= (
        ('Male','Male'),
        ('Female','Female')
        )
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    # Here we add the extra form fields that we will use to create another model object
    gender = forms.ChoiceField(choices = GENDER_CHOICE, required=True)
    profile_pic = forms.ImageField(required=False)
 
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]