from django.urls import path
from . import views

urlpatterns = [
    # path("ratings", views.RatingsView.as_view()),
    path("", views.holamundo, name=""),
    path("books", views.get_books, name="books"),
    path("books/<int:id>", views.get_book_id, name="book_id"),
]
