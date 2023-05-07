from django.urls import path
from user_directory.views import home
from .views import user_profile

urlpatterns = [
    path('profiile/', user_profile, name='user_profile'),

]
