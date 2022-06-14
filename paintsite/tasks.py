from celery import shared_task
# from celery.task import task
from django.conf import settings
from django.core.mail import send_mail
from .models import Comment, User
import datetime
from paintweb.celery import app


@shared_task(bind=True)
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


@app.task(bind=True, ignore_result=True, name='paintsite.tasks.send_comment_notification',
          default_retry_delay=120, max_retries=5,
          soft_time_limit=120, time_limit=125)
def send_comment_notification(user: User, comment: Comment):
    print("Here we are")
    mail_subject = "You have new comment."
    to_email = user.email
    message = 'You received comments from ' + comment.author

    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return True
