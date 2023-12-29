from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            # messages.error(request, 'Successfully Logged In.')
            return redirect('home')
        else:
            messages.error(request, 'Please provide valid credentials!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


@login_required(login_url='login')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')
    else:
        messages.error(request, 'You must be logged in!')
        return redirect('login')


def org_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is Already Taken.')
            return redirect('signup')
        else:
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            org = Organization()
            org.user = user
            org.organization_name = request.POST.get('name')
            org.email = request.POST.get('email')
            org.service_needed = request.POST.get('service_needed')
            org.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('login')

    return render(request, 'accounts/org_signup.html')



def vol_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is Already Taken.')
            return redirect('signup')
        else:
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            vol = Volunteer()
            vol.user = user
            vol.name = request.POST.get('name')
            vol.email = request.POST.get('email')
            vol.number = request.POST.get('number')
            vol.resume = request.FILES.get('resume')
            vol.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('login')

    return render(request, 'accounts/vol_signup.html')
