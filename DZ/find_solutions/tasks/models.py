from django.db import models
from django.contrib.auth.models import User

# Create your models here.
f = (
    ('1', 'PK1'),
    ('2', 'PK2'),
    ('3', 'PK3'),

)


class Task(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    memo_images = models.ImageField(upload_to="memo/%Y/%m/%d/", blank=True)
    decision = models.TextField(blank=True)
    decision_images = models.ImageField(upload_to="decision/%Y/%m/%d/", blank=True)
    created = models.DateField(auto_now_add=True)
    data_complete = models.DateField(blank=True, null=True)
    line = models.CharField(max_length=100, choices=f,default='PK1')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
