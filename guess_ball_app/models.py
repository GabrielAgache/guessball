from django.contrib.auth.models import User
from django.db import models


class Competition(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    buy_date = models.DateTimeField()
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)


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
