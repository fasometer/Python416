from django.db import models


# Create your models here.

class Site_one(models.Model):
    title = models.CharField()
    descriptions = models.CharField()
    image = models.ImageField('site_one/images/')
    url = models.URLField(blank=True)

