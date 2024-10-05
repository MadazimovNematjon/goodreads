from django.urls import path

from .views import BookListView, BookDetailView, AddReviewView

urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('<int:pk>/reviews/', AddReviewView.as_view(), name='reviews'),
]
