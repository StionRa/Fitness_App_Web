from django.urls import path
from .views import home, login_page, register_page, check_username


urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('', home, name='home'),
    path('check_username/', check_username, name='check_username'),
]
