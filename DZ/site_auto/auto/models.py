from django.db import models


# Create your models here.
class Automat(models.Model):
    title = models.CharField()
    description = models.CharField()
    image = models.ImageField('auto/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
