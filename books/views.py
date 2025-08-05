from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter
from .models import BookTable, UserTable, UserRatingTable
from .serializers import BookTableSerializer, UserTableSerializer, UserCreateSerializer, UserBookRatingSerializer, UserBookRatingCreateSerializer


# Create your views here.
class BookListView(ListAPIView):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


class UserListView(ListAPIView):
    queryset = UserTable.objects.all()
    serializer_class = UserTableSerializer

class UserCreateView(CreateAPIView):
    queryset = UserTable.objects.all()
    serializer_class = UserCreateSerializer


class UserBookRatingView(ListAPIView):
    serializer_class = UserBookRatingSerializer

    def get_queryset(self):
        queryset = UserRatingTable.objects.select_related("userID", "bookID").all()
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(userID__username = username)
        return queryset

class UserBookRatingCreateView(CreateAPIView):
    serializer_class = UserBookRatingCreateSerializer

