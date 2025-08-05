from django.urls import path
from .views import BookListView, UserListView, UserCreateView, UserBookRatingView, UserBookRatingCreateView

urlpatterns = [
    path("books/", BookListView.as_view(), name = "book-list"),
    path("users/", UserListView.as_view(), name = "user-list"),

    path("users/add/", UserCreateView.as_view(), name = "user-create"),
    path('ratings/', UserBookRatingView.as_view(), name='user-rated-books'),

    path('ratings/add/', UserBookRatingCreateView.as_view(), name='user-rating-create')
]
