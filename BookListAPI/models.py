from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    thematic = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    value = models.FloatField()
    published_date = models.DateField()
