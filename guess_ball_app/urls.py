from django.contrib import admin
from django.urls import path, include

from guess_ball_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('faq/', views.faq, name="faq"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
]
