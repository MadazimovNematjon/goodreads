from django.core.mail import send_mail
from goodreads_2.celary import app
from celery import shared_task





@app.task
def send_email(subject, message, recipient_list):
    print(f"Sending email with subject: {subject}, message: {message}, recipient: {recipient_list}")

    send_mail(
        subject,
        message,
        "<EMAIL>",
        recipient_list,
    )
    # Email jo'natish logikasi shu yerda
    return True  # yoki email jo'natish natijasi

