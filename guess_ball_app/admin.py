from django.contrib import admin

# Register your models here.
from guess_ball_app.models import Faq, AboutInfo

admin.site.register(Faq)
admin.site.register(AboutInfo)