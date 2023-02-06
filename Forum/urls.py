from django.contrib import admin
from django.urls import path
from Forum import views

urlpatterns = [
    path('', views.index),
    path('Register', views.signup),
    path('Login',views.login)
]