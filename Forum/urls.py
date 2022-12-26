from django.contrib import admin
from django.urls import path
from Forum import views

urlpatterns = [
    path('', views.index),
    path('Sign-up', views.signup),
    path('login',views.login)
]