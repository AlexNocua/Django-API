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
    # category = CategorySerializer()
    # category = CategorySerializer(read_only = True)
    # category_id = serializers.IntergerField(write_only = True)
    """
    Creacion de vinculo para visualizar el contenido de una relacion desde un hipervinculo
    """
    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(), view_name="category-detail"
    # )

    class Meta:
        model = Book
        fields = ["stock", "value_after_tax", "category", "author"]
        # depth = 1 # muestra el serializador de la categoria con con el mismo modo de asignar el serializador de la categoria dentro del la variable categoria.

    def calculate_tax(self, product: Book):
        return int(product.value) * Decimal(1.1)
