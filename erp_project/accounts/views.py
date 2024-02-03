from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from erp_app.models import Letter
from django.contrib.auth.models import Group, User


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            normal_user_group = Group.objects.get(name='normaluser')
            user.groups.add(normal_user_group)
            user.save()

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@user_passes_test(lambda u: is_in_group(u, 'ceo'))
def ceo_dashboard(request):
    ceo_letters = Letter.objects.filter(recipient='ceo')
    return render(request, 'ceo_dashboard.html', {'ceo_letters': ceo_letters})


@user_passes_test(lambda u: is_in_group(u, 'cto'))
def cto_dashboard(request):
    cto_letters = Letter.objects.filter(recipient='cto')
    return render(request, 'cto_dashboard.html', {'cto_letters': cto_letters})


@user_passes_test(lambda u: is_in_group(u, 'pm'))
def pm_dashboard(request):
    pm_letters = Letter.objects.filter(recipient='pm')
    return render(request, 'pm_dashboard.html', {'pm_letters': pm_letters})


@user_passes_test(lambda u: is_in_group(u, 'admin'))
def admin_dashboard(request):
    all_letters = Letter.objects.all()
    return render(request, 'admin_dashboard.html', {'all_letters': all_letters})
