from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    lines = models.ForeignKey('Lines', on_delete=models.CASCADE, default="")
    place = models.ForeignKey('Place', on_delete=models.CASCADE, default="")
    memo = models.TextField(blank=True)
    memo_images = models.ImageField(upload_to="memo/%Y/%m/%d/", blank=True)
    decision = models.TextField(blank=True)
    decision_images = models.ImageField(upload_to="decision/%Y/%m/%d/", blank=True)
    created = models.DateField(auto_now_add=True)
    data_complete = models.DateField(blank=True, null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lines(models.Model):
    line = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.line


class Place(models.Model):
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.place
