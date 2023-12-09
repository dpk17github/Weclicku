from django.shortcuts import redirect,render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')