from django.urls import include, path
from . import views


urlpatterns = [
    # path("", views.view_init, name=""),
    # path("books", views.BookList.as_view()),
    #  path("books/book/<int:pk>", views.Book.as_view()),
    path("books", views.BookList.as_view()),
    path("books/<str:name>", views.BookDetail.as_view(), name= "book-details"),
    path("__debug__/", include("debug_toolbar.urls")),
]
