from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import library


# cambia una instancia Query a un objeto
from django.forms.models import model_to_dict


# def create_book():
#     model = library(
#         title="The hole black", author="Stephen Howking", price=2.33, inventory=1
#     )
#     model.save()
#     return "Save"


# Create your views here.
def holamundo(request):
    return HttpResponse("buenas")


def get_books(request):
    data = library.objects.all()
    data_dict = {content.id: model_to_dict(content) for content in data}
    data_json = JsonResponse(data_dict, safe=False)
    print(data_json)
    if data:
        return HttpResponse(data_json)
    else:
        error = FileExistsError
        return HttpResponse()


def get_book_id(request, id):
    data = library.objects.get(id=id)
    data_dict =  model_to_dict(data)
    data_json = JsonResponse(data_dict)
    if data_json:
        return HttpResponse(data_json)
    else:
        error = FileExistsError
        return HttpResponse(error)
