from django.shortcuts import render
from django.views import View

from books.models import Book


# Create your views here.


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, template_name='books/books.html', context=context)
