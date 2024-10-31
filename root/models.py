from django.db import models
from django.contrib.auth.models import  User 


class Testimonials(models.Model):
    content = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name

class Pros(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title

class Prices(models.Model):
    title = models.CharField( max_length=50)
    price = models.IntegerField(default=0)
    pros = models.ManyToManyField(Pros)
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title

class FQA(models.Model):
    title = models.TextField(max_length=120)
    answer = models.TextField(max_length=250)
    def __str__(self) -> str:
        return self.title

class Services(models.Model):
    title = models.TextField()
    desc = models.TextField()
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title


class Services_two(models.Model):
    title = models.TextField()
    desc = models.TextField()
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title
