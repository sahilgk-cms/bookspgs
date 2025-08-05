from rest_framework import serializers
from .models import BookTable, UserTable, UserRatingTable


class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = "__all__"



class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ["username"]


class UserBookRatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='userID.username')
    title = serializers.CharField(source='bookID.title')

    class Meta:
        model = UserRatingTable
        fields = ["username", "title", "rating"]


class UserBookRatingCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    bookID = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserRatingTable
        fields = ['username', 'bookID', 'rating']

    def create(self, validated_data):
        username = validated_data['username']
        bookID = validated_data['bookID']
        rating = validated_data['rating']

        try:
            user = UserTable.objects.get(username = username)
        except UserTable.DoesNotExist:
            raise serializers.ValidationError("User does not exist")

        try:
            book = BookTable.objects.get(bookID = bookID)
        except BookTable.DoesNotExist:
            raise serializers.ValidationError("Book does not exist")

        obj, created = UserRatingTable.objects.get_or_create(userID = user,
                                                             bookID = book,
                                                             defaults = {"rating": rating})
        return obj


