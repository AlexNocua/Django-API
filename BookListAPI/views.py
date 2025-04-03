from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

from django.db.models import Q


# Create your views here.
# @api_view(["POST", "GET"])
# def view_init(request):
#     return Response("List of books", status=status.HTTP_200_OK)


# Vistas basadas en clases
# ejemplo de una vista basada en clases con algunos de los metodos de la misma
"""
importante recordar como se definen este tipo de vistas en las urls
"""


# class BookList(APIView):
#     def get(self, request):
#         author = request.GET.get("author")
#         if author:
#             return Response(
#                 {"message": f"List of the books by {author}"},
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 {"message": f"List of the books"},
#                 status=status.HTTP_200_OK,
#             )

#     def post(self, request):
#         return Response({"message": "new book create"}, status=status.HTTP_201_CREATED)


# class Book(APIView):
#     def get(self, request, pk):
#         return Response(
#             {"message": f"Single book with id {pk}"}, status=status.HTTP_200_OK
#         )

#     def put(self, request, pk):
#         return Response({"title": request.data.get("title")}, status=status.HTTP_200_OK)


# clases funcionales utilizando vistas basadas en clases con APIView


class BookList(APIView):
    def get(self, request):
        """ "
        Modo de busqueda sin DRF
        """
        # author = request.GET.get("author")
        # if author:
        #     books = Book.objects.filter(Q(author__icontains=author))
        #     if books:
        #         message = f"Operacion Exitosa."

        #     else:
        #         message = f"No fue  encontrado ningun libro relacionado con el autor {author}."
        #         books = Book.objects.select_related("category").all()
        #     serializer = BookSerializer(books, many=True)
        #     return Response(
        #         {"message": f"{message}", "data": serializer.data},
        #         status=status.HTTP_200_OK,
        #     )

        """
        Busqueda con DRF
        """
        books = Book.objects.select_related("category").all()
        author = request.query_params.get("author")
        if author:

            books = books.filter(author__icontains=author)
            if books:
                message = f"El autor {author} fue encontrado. "
            else:
                message = f"El autor {author} no fue encontrado. "

            serializer = BookSerializer(books, many=True)
            return Response(
                {"message": f"{message}", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        else:
            books = Book.objects.all()
            message = "No se proporcionaron parámetros de búsqueda."
            # serializer = BookSerializer(books, many=True)
            # ajustes en el serializador para configurar links de acceso a relaciones serializadas
            #######################################
            serializer_item = BookSerializer(
                books, many=True, context={"request": request}
            )
            #######################################
            return Response(
                {"message": message, "data": serializer_item.data},
                status=status.HTTP_200_OK,
            )

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get(self, request, name):
        book = Book.objects.filter(name__icontains=name)
        if book.exists():
            message = "Busqueda Existosa"
            serializer = BookSerializer(book, many=True)
            return Response(
                {"message": message, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            message = f"El libro con el nombre {name} no fue encontrado."
            return Response(
                {"message": message, "data": {}},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, name):
        book = Book.objects.get(name__icontains=name)
        serializer = BookSerializer(book, data=request.data, partial=True)
        datos_antiguos = BookSerializer(book).data
        if serializer.is_valid():
            serializer.save()
            message = f"Datos anteriores: {datos_antiguos}, Datos Actualizados: {request.data}"
            return Response(
                {"message": message, "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        message = f"El libro con el nombre {name} no fu encontrado."
        return Response(
            {"message": message, "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, name):
        book = Book.objects.get(name__icontains=name)
        book.delete()
        return Response(
            {"message": f"El libro con el nombre {name} fue eliminado correctamente."},
            status=status.HTTP_200_OK,
        )


# ejemplo de vista de muestra de datos de relaciones por medio de hipervinculos
@api_view()
def caregory_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data, status=status.HTTP_200_OK)
