from django.db import models

# Create your models here.
class BookTable(models.Model):
    bookID = models.IntegerField(primary_key=True)
    title = models.TextField()
    authors = models.TextField()
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=20)
    isbn13 = models.CharField(max_length=20)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.TextField()
    publisher = models.TextField()

    class Meta:
        managed = False
        db_table = "booktable"


class UserTable(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)

    class Meta:
        managed = False
        db_table = 'usertable'


class UserRatingTable(models.Model):
    userID = models.ForeignKey(UserTable, on_delete=models.CASCADE, db_column='userID', primary_key=True)
    bookID = models.ForeignKey(BookTable, on_delete=models.CASCADE, db_column='bookID')
    rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'userratingtable'
        unique_together = (('userID', 'bookID'),)