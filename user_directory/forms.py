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
        self.fields['username'].widget.attrs.update(
            {'type': "text", 'class': "form-control", 'id': "id_username", 'placeholder': "Username"})
        self.fields['email'].widget.attrs.update(
            {'type': "email", 'class': "form-control", 'id': "floatingInput", 'placeholder': 'E-Mail'})
        self.fields['password1'].widget.attrs.update(
            {"name": "password1", "type": "password", "id": "floatingPassword", 'class': 'form-control',
             'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {"name": "password2", "type": "password", "id": "floatingPassword", 'class': 'form-control',
             'placeholder': 'Confirm Password'})


GENDER_TYPE_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("N", "None"),
]

BODY_TYPE_CHOICES = [
    ("Endo", "Endomorph"),
    ("Meso", "Mesomorph"),
    ("Ecto", "Ectomorph"),
]

ACTIVITY_LEVEL_CHOICES = [
    ("Bed", "Bed rest"),
    ("Sed", "Sedentary"),
    ("Lig", "Light exercise"),
    ("Mod", "Moderate exercise"),
    ("Hea", "Heavy exercise"),
    ("Ver", "Very heavy exercise"),
]


class ProfileUpdateForm(forms.ModelForm):
    activity_level = forms.ChoiceField(choices=ACTIVITY_LEVEL_CHOICES, widget=forms.Select(
        attrs={"name": "activity_level", "id": "form-select", 'class': 'form-select', 'placeholder': 'Activity level'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE_CHOICES, widget=forms.Select(
        attrs={"name": "gender", "id": "form-select", 'class': 'form-select', 'placeholder': 'Gender'}))
    body_type = forms.ChoiceField(choices=BODY_TYPE_CHOICES, widget=forms.Select(
        attrs={"name": "body_type", "id": "form-select", 'class': 'form-select', 'placeholder': 'Body type'}))

    class Meta:
        model = Profile
        fields = ['image', 'biography', 'body_height', 'body_weight', 'birth_day', 'gender', 'body_type', 'activity_level',
                  'target_weight', 'time_to_goal']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['biography'].widget.attrs.update(
            {'name': 'biography', 'type': "text", 'class': "form-control", 'id': "floatingInput",
             'placeholder': "Biography"})
        self.fields['body_height'].widget.attrs.update(
            {'name': 'body_height', 'type': "text", 'class': "form-control", 'id': "floatingInput",
             'placeholder': 'Body height'})
        self.fields['body_weight'].widget.attrs.update(
            {"name": "body_weight", "type": "text", "id": "floatingInput", 'class': 'form-control',
             'placeholder': 'Body weight'})
        self.fields['birth_day'].widget = forms.DateInput(attrs={
            "name": "birth_day", "class": "form-control", "placeholder": "Birthday", "type": "date"
        })
        self.fields['target_weight'].widget.attrs.update(
            {"name": "target_weight", "type": "text", "id": "floatingInput", 'class': 'form-control',
             'placeholder': 'Target weight'})
        self.fields['time_to_goal'].widget.attrs.update(
            {"name": "time_to_goal", "type": "text", "id": "floatingInput", 'class': 'form-control',
             'placeholder': 'Time to goal'})
