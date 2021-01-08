from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from guess_ball_app.forms import SignUpForm
from guess_ball_app.models import Faq, AboutInfo, Competition

def error_404(request, exception):
    return render(request, 'guess_ball_app/404.html')

def home(request):
    return render(request, "guess_ball_app/home.html")


def faq(request):
    all_faqs = Faq.objects.all()
    return render(request, "guess_ball_app/faq.html", {"all_faqs": all_faqs})


def aboutus(request):
    all_about = AboutInfo.objects.all()
    return render(request, "guess_ball_app/aboutus.html", {"all_about": all_about})


def contact(request):
    return render(request, "guess_ball_app/contact.html")


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'guess_ball_app/templates/registration/login.html', {'sign_up_form': form})
    else:
        return redirect('login')


@login_required
def profile(request):
    return render(request, 'guess_ball_app/profile.html')


def competitions(request):
    return render(request, 'guess_ball_app/competitions.html')


@login_required
def competition(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    return render(request, 'guess_ball_app/competition.html', {'competition': competition})