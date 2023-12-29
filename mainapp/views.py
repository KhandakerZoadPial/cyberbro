from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def research(request):
    return render(request, 'mainapp/research.html')


def about(request):
    return render(request, 'mainapp/about.html')