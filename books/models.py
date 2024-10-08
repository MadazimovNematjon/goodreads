from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    cover_image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.full_name()


    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE ,related_name='books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='authors')

    def __str__(self):
        return f"{self.author}  {self.book}"




class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review_text = models.TextField()
    stars_given = models.PositiveSmallIntegerField(
                                                   validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.author}  {self.book}  {self.review_text}"
