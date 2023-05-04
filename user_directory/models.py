from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    biography = models.TextField(max_length=500, null=True, blank=True)
    body_height = models.DecimalField(max_digits=5, decimal_places=2, default=1.80)
    body_weight = models.DecimalField(max_digits=5, decimal_places=2, default=74)

    birth_day = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(default=25)
    GENDER_TYPE_CHOICE = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "None"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_TYPE_CHOICE, default="N")
    BODY_TYPE_CHOICE = [
        ("Endo", "Endomorph"),
        ("Meso", "Mesomorph"),
        ("Ecto", "Ectomorph"),
    ]
    body_type = models.CharField(max_length=4, choices=BODY_TYPE_CHOICE, default="1")
    ACTIVITY_LEVEL_CHOISE = [
        ("Bed", "Bed rest"),
        ("Sed", "Sedentary"),
        ("Lig", "Light exercise"),
        ("Mod", "Moderate exercise"),
        ("Hea", "Heavy exercise"),
        ("Ver", "Very heavy exercise"),
    ]
    activity_level = models.CharField(max_length=3, choices=ACTIVITY_LEVEL_CHOISE, default="1")
    target_weight = models.DecimalField(max_digits=5, decimal_places=2, default=75)
    time_to_goal = models.IntegerField(default=180)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, default=19.75)

    def __str__(self):
        return str(self.user)
