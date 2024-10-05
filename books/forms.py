from django import forms

from books.models import BookReview


class BookForm(forms.ModelForm):
    pass


class BookReviewForm(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5, min_value=1, )

    class Meta:
        model = BookReview
        fields = ['review_text', 'stars_given']
