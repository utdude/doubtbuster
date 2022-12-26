from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "Signup.html")

def login(request):
    return render(request, "Login.html")