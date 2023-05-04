from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        image = forms.ImageField()
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography', 'body_height', 'body_weight', 'birth_day', 'gender', 'body_type', 'activity_level',
                  'target_weight', 'time_to_goal']
