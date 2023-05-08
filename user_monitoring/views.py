from user_directory.models import Profile
from django.contrib.auth.decorators import login_required
from .utils import calculate_age, calculate_bmr, calculate_bmi


@login_required
def calculate(request):
    user_profile = Profile.objects.get(user=request.user)

    if user_profile.body_height and user_profile.body_weight and user_profile.birth_day and user_profile.gender \
            and user_profile.activity_level:
        birth_date = user_profile.birth_day
        age = calculate_age(birth_date)
        user_profile.age = age
        user_height = user_profile.body_height
        user_weight = user_profile.body_weight
        bmi = calculate_bmi(user_height, user_weight)
        user_profile.bmi = bmi
        user_gender = user_profile.gender
        user_activity = user_profile.activity_level
        bmr = calculate_bmr(age, user_gender, user_weight, user_height, user_activity)
        user_profile.bmr = bmr
        user_profile.save()

