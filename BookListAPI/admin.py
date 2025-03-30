from django.contrib import admin
from .models import Book
from django.contrib import admin

# Register your models here.


@admin.register(Book)
class ModelObjetivoGeneralAdmin(admin.ModelAdmin):
    list_display = ("author", "name")
    search_fields = ("author",)
