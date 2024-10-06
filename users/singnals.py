from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser



@receiver(post_save, sender=CustomUser)
def sender_welcome_email(sender, instance, created, **kwargs):
    print("sender_welcome_email")
    if created:
        # user create bolgada email jonatiladi
        # send_mail(
        #     "Welcome to Goodreads",
        #     f"Hi {instance.username}. Welcome to Goodreads Enjoy th books and review",
        #     "nmadazimov734@gmail.com",
        #     [instance.email],
        # )
        pass