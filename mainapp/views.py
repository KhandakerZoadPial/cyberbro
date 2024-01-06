from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def research(request):
    return render(request, 'mainapp/research.html')


def about(request):
    return render(request, 'mainapp/about.html')


def profile(request):
    user = request.user
    if user.is_authenticated:
        context = {

        }
        print(Volunteer.objects.all())
        
        if Volunteer.objects.filter(user=user).count() > 0:
            vol = Volunteer.objects.filter(user=user)[0]
            context['user_type'] = 'Volunteer'
            context['profile'] = vol
        else:
            org = Organization.objects.filter(user=user)[0]
            context['user_type'] = 'Organization'
            context['profile'] = org
        
        return render(request, 'mainapp/profile.html', context)
    else:
        return redirect('login')


def all_vol(request):
    context = {
        'vol_set': Volunteer.objects.all()
    }
    return render(request, 'mainapp/all_vol.html', context)


def all_org(request):
    context = {
        'org_set': Organization.objects.all()
    }
    return render(request, 'mainapp/all_org.html', context)


def view_profile(request, user_id):
    context = {

    }
    user = User.objects.get(pk=user_id)
    if Volunteer.objects.filter(user=user).count() > 0:
        vol = Volunteer.objects.filter(user=user)[0]
        context['user_type'] = 'Volunteer'
        context['profile'] = vol
    else:
        org = Organization.objects.filter(user=user)[0]
        context['user_type'] = 'Organization'
        context['profile'] = org
    
    return render(request, 'mainapp/profile.html', context)
        