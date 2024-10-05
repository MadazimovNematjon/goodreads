from django.shortcuts import render

from books.models import BookReview


def landing(request):
    return render(request, 'landing.html')


def home_page(request):
    book_reviews = BookReview.objects.all().order_by('-created_at')
    context = {'book_reviews': book_reviews}
    return render(request, 'home.html',context)
