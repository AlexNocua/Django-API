from decimal import Decimal
from .models import Book, Category
from rest_framework import serializers


# class BookSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField()

#     class Meta:
#         model = Book
#         fields = "__all__"
#         # fields = ["name"], #en este se pueden monstrar cada  uno de los datos que quiera mostrar en la API


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description_category"]


class BookSerializer(serializers.ModelSerializer):

    stock = serializers.IntegerField(source="value")
    value_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # category = serializers.StringRelatedField()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ["stock", "value_after_tax", "category"]

    def calculate_tax(self, product: Book):
        return int(product.value) * Decimal(1.1)
