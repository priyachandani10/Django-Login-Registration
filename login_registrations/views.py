from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "login_registrations/index.html")

def signup(request):
    return render(request, "login_registrations/signup.html")

def signin(request):
    return render(request, "login_registrations/signin.html")

def signout(request):
    pass