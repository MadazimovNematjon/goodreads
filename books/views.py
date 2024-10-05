from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm
from books.models import Book, BookReview


# Create your views here.

# class BookListView(ListView):
#     template_name = 'books/books.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'


# class BookDetailView(DetailView):
#     template_name = 'books/book_detail.html'
#     pk_url_kwarg = 'pk'
#     model = Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 8)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        pages = paginator.get_page(page_num)

        context = {'pages': pages}
        return render(request, template_name='books/books.html', context=context)


class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)

        review_form = BookReviewForm()

        context = {
            'book': book,
            'review_form': review_form,
        }
        return render(request, template_name='books/book_detail.html', context=context)


# class AddReviewView(LoginRequiredMixin, View):
#     def post(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         review_form = BookReviewForm(request.POST)
#         if review_form.is_valid():
#             BookReview.objects.create(
#                 book=book,
#                 user=request.user,
#                 stars_given=review_form.cleaned_data['stars_given'],
#                 review_text=review_form.cleaned_data['review_text'],
#             )
#             return redirect(reverse('books:book_detail', kwargs=['pk', book.pk]))
#         context = {
#             'book': book,
#             'review_form': review_form,
#         }
#         return render(request, template_name='books/book_detail.html', context=context)
#

class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        review_form = BookReviewForm(request.POST)
        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                author=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                review_text=review_form.cleaned_data['review_text'],
            )
            return redirect(reverse('detail', kwargs={'pk': pk}))
        context = {
            'book': book,
            'review_form': review_form,
        }
        return render(request, 'books/book_detail.html', context)
