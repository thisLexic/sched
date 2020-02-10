from django.shortcuts import render

def landing_page(request):
    return render(request,"landing_page.html")

def login(request):
    return render(request,"login.html")

def create_user(request):
    return render(request,"create_user.html")

def dates(request):
    return render(request,"dates.html")

def times(request):
    return render(request,"times.html")

