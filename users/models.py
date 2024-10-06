from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile',null=True,blank=True,
                                        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])

