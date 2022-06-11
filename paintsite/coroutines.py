from asgiref.sync import sync_to_async

from paintsite.models import PictureBoard, Comment


@sync_to_async
def get_pps(**kwargs):
    return PictureBoard.objects.filter(**kwargs)


@sync_to_async
def get_comments(**kwargs):
    return Comment.objects.filter(**kwargs)
