from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': "text", 'class': "form-control", 'id': "floatingInput", 'placeholder': "username"})
        self.fields['email'].widget.attrs.update({'type': "email", 'class': "form-control", 'id': "floatingInput", 'placeholder': 'E-Mail'})
        self.fields['password1'].widget.attrs.update({"name": "password1", "type": "password", "id": "floatingPassword", 'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({"name": "password2", "type": "password", "id": "floatingPassword", 'class': 'form-control', 'placeholder': 'Confirm Password'})


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography', 'body_height', 'body_weight', 'birth_day', 'gender', 'body_type', 'activity_level',
                  'target_weight', 'time_to_goal']
