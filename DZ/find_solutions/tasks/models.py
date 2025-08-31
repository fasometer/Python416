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


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', 'created']
