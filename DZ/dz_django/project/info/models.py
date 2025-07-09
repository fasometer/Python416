from django.db import models


# Create your models here.

class Info(models.Model):
    title = models.CharField()
    descriptions = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
