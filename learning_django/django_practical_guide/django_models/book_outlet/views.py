from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Avg
from .models import Book

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": books.count(),
        "average_rating": books.aggregate(Avg("rating"))
    })

def book_detail(request: HttpRequest, id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling 
    })
