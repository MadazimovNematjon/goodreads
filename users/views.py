from lib2to3.fixes.fix_input import context

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationForm, UserLoginForm, UserUpdateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreationForm()
        context = {'form': create_form}
        return render(request, 'users/register.html', context)

    def post(self, request):
        # create user
        create_form = UserCreationForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            print("save user")

            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': create_form})


class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm(request.POST)
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            username = login_form.get_user()
            print(username)

            login(request, username)
            return redirect('home')
        else:
            return render(request, 'error.html', {'login_form': login_form})


class ProfileView(View):
    def get(self, request):
        user = request.user
        context = {'profile': user}
        if user.is_authenticated:
            return render(request, 'users/profile.html', context)

        return redirect('login')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        context = {'user_update_form': user_update_form}
        return render(request, 'users/profile_edit.html', context=context)


    def post(self, request):
        user_update_form = UserUpdateForm(request.POST, instance=request.user,files=request.FILES)

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')


        return render(request, 'users/profile_edit.html', {'user_update_form': user_update_form})
