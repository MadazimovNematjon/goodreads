from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book


# Create your views here.

# class BookListView(ListView):
#     template_name = 'books/books.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'


class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'pk'
    model = Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        paginator = Paginator(books, 8)

        page_num = request.GET.get('page', 1)
        pages = paginator.get_page(page_num)
        context = {'pages': pages}
        return render(request, template_name='books/books.html', context=context)

# class BookDetailView(View):
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         return render(request, template_name='books/book_detail.html', context={'book': book})
