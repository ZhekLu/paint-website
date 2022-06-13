from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Comment, User
import datetime


@shared_task
def comments_notification():
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    comments = Comment.objects.filter(created_at__gte=date_from)
    mail_subject = "New comments for today."
    users = dict()
    for comment in comments:
        u = comment.pp.author.pk
        if u in users.keys():
            users[u].add(comment.author)
        else:
            users[u] = {comment.author, }

    for pk, receivers in users.items():
        user = User.objects.get(pk=pk)
        if not user.send_messages:
            continue
        to_email = user.email
        message = 'You received comments from ' + ', '.join([receiver for receiver in receivers])
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return True
