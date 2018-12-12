from typing import Dict

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Box
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import MyUserLoginForm, MyUserRegistrationForm

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .forms import CreateBox

from .filters import BoxFilters


# Create your views here.


class Boxview(ListView):
    model = Box
    template_name = 'accounts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BoxFilters(self.request.GET, queryset=self.get_queryset())
        return context


class BoxUpdate(UpdateView):
    model = Box
    fields = ['']
@login_required(login_url='accounts:login')
def user_post(request):
    user = request.user
    user_posts = Box.objects.filter(author=request.user)
    return render(request, 'accounts/user_post.html', {'user_posts': user_posts, 'user': user})


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
        return redirect('accounts:list')
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
            return redirect('accounts:list')
        return render(request, 'accounts/signup.html', {'form': form})
    else:
        return redirect('accounts:list')


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('accounts:logout')


def create_box(request):
    form = CreateBox(request.POST or None, request.FILES or None)

    if form.is_valid():
        Box = form.save(commit=False)
        Box.author = request.user
        Box.save()
        return redirect('accounts:list')

    context = {
        'form': form
    }

    return render(request, 'accounts/create_box.html', context)


