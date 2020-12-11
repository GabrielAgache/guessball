from django.urls import path

from guess_ball_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('faq/', views.faq, name="faq"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
    path('login/', auth_views.LoginView.as_view(template_name='guess_ball_app/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('profile/', views.profile, name='profile'),
    path('competitions/', views.competitions, name="competitions")
]
