from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import user_monitoring.views
from .forms import CreateUserForm, ProfileUpdateForm
from .models import Profile
from django.db import transaction
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'user_directory/home.html')


class HomePageView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'user_directory/home.html'

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home')


def about_page(request):
    return render(request, 'user_directory/about.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' wellcome {username} !!')
            user_monitoring.views.calculate(request)
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = CreateUserForm()
    return render(request, 'user_directory/login.html', {'form': form, 'title': 'log in'})


@transaction.atomic
def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, f'The username {username} is already taken.')
            if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                form.add_error('password2', 'Passwords do not match')
            else:
                user_form = form.save()
                profile_user = Profile.objects.create(user=user_form)
                form_u = ProfileUpdateForm(request.POST, instance=profile_user)
                if form_u.is_valid():
                    form_u.save()
                messages.success(request, f'Your account has been created. You can log in now!')
                return redirect('home')
        else:
            # Если форма не валидна, то возвращаем ошибку
            messages.error(request, 'Form is not valid')
            return redirect('register')
    else:
        form = CreateUserForm()
        form_u = ProfileUpdateForm()
        return render(request, 'user_directory/register.html', {'form': form, 'form_u': form_u})


def check_username(request):
    """
    Проверяет, свободно ли имя пользователя.
    """
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def logout_view(request):
    logout(request)
    return redirect('login')
