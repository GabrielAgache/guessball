from django.db import models


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question


class AboutInfo(models.Model):
    title = models.CharField(max_length=30)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
