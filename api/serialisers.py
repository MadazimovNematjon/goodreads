from rest_framework import  serializers


class BookReviewsSerializer(serializers.Serializer):
    stars_given = serializers.IntegerField(min_value=1, max_value=5)