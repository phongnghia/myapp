from django.contrib import admin
from django.db import models


# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_type = models.CharField(max_length=200)
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name
