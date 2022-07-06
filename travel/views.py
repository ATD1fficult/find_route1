from django.shortcuts import render


def home(request):
    name = 'Ivan'
    return render(request, 'home.html')

def about(request):
    name = 'Ivan'
    return render(request, 'about.html')