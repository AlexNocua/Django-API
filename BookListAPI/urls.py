from django.urls import path
from . import views


urlpatterns = [
    # path("", views.view_init, name=""),
    path("books", views.BookList.as_view()),
    path("books/book/<int:pk>", views.Book.as_view()),
]
