from datetime import datetime
from os.path import splitext

from django.core.mail import send_mail
from django.core.signing import Signer
from django.template.loader import render_to_string
from django.conf import settings

signer = Signer()


def send_activation_notification(user):
    if settings.ALLOWED_HOSTS:
        host = 'https://' + settings.ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'

    context = {'user': user, 'host': host,
               'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    message = render_to_string('email/activation_letter_body.txt', context)
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email, ],
        fail_silently=True
    )


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
