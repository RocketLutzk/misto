from typing import Dict

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .forms import MyUserLoginForm, MyUserRegistrationForm

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .forms import CreateBox


# Create your views here.
@login_required(login_url='accounts:login')
def home(request):
    return render(request, 'accounts/home.html', {})


def login_view(request):
    next = request.GET.get('next')
    form = MyUserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('accounts:home')
    return render(request, 'accounts/login.html', {'form': form})


def registration_view(request):
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        form = MyUserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email1')
            user.set_password(password)
            user.email = email
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect('accounts:home')
        return render(request, 'accounts/signup.html', {'form': form})
    else:
        return redirect('accounts:home')


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('accounts:home')


def create_box(request):
    form = CreateBox(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('accounts:home')

    context = {
        'form': form
    }

    return render(request, 'accounts/create_box.html', context)
