from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response


# Create your views here.
# @api_view(["POST", "GET"])
# def view_init(request):
#     return Response("List of books", status=status.HTTP_200_OK)


# Vistas basadas en clases
# ejemplo de una vista basada en clases con algunos de los metodos de la misma
"""
importante recordar como se definen este tipo de vistas en las urls
"""


class BookList(APIView):
    def get(self, request):
        author = request.GET.get("author")
        if author:
            return Response(
                {"message": f"List of the books by {author}"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": f"List of the books"},
                status=status.HTTP_200_OK,
            )

    def post(self, request):
        return Response({"message": "new book create"}, status=status.HTTP_201_CREATED)


class Book(APIView):
    def get(self, request, pk):
        return Response(
            {"message": f"Single book with id {pk}"}, status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        return Response({"title": request.data.get("title")}, status=status.HTTP_200_OK)
