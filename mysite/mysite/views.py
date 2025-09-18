
from django.shortcuts import render

from books.models import Book


def home(request):
    books=Book.objects.all()
    return render(request,'home.html', context= {'books':books})
