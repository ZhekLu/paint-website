from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Was activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Want to get messages about new comments?')

    class Meta(AbstractUser.Meta):
        pass