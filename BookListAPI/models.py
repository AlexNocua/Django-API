from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description_category = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    thematic = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    value = models.FloatField()
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
