from django.db import models


# Create your models here.
class Show(models.Model):
    title = models.CharField()
    description = models.CharField()
    image = models.ImageField('show/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
