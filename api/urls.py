from django.urls import path

from api.views import BookReviewAPIView

app_name='api'
urlpatterns = [
    path('reviews/<int:pk>',BookReviewAPIView.as_view())
]
