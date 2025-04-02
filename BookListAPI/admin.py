from django.contrib import admin
from .models import Book, Category
from django.contrib import admin

# Register your models here.


@admin.register(Book)
class ModelObjetivoGeneralAdmin(admin.ModelAdmin):
    list_display = ("author", "name")
    search_fields = ("author",)

@admin.register(Category)
class ModelCategoryAdmin(admin.ModelAdmin):
    list_display=("name","description_category")