from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_profile(request):
    user_data = request.user.profile
    return render(request, 'user_profil/user_profile.html', {'profile': user_data})
