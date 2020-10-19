from django.shortcuts import render

from guess_ball_app.models import Faq, AboutInfo


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