from django.urls import path
from .views import home, login_page, logout_view, register_page, check_username, about_page

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('logout/', logout_view, name='logout'),
    path('about/', about_page, name='about'),
    path('check_username/', check_username, name='check_username'),
]
