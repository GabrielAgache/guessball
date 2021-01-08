from django.urls import path, include

from guess_ball_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('faq/', views.faq, name="faq"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('profile/', views.profile, name='profile'),
    path('competitions/', views.competitions, name="competitions"),
    path('competitions/<int:competition_id>', views.competition, name="competition")
]
