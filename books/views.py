from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


# Create your views here.


def ListBooks(request):
    request = Book.objects.get(id=1)
    books = request
    return HttpResponse(books)
