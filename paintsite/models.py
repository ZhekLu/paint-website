from django.db import models
from django.contrib.auth.models import AbstractUser

from paintsite.utilities import get_timestamp_path


class User(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Was activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Want to get messages about new comments?')

    def delete(self, *args, **kwargs):
        for post in self.pictureboard_set.all():
            post.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass


# Tag models


class Tag(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Designation')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Order')
    super_tag = models.ForeignKey('SuperTag', on_delete=models.PROTECT, null=True, blank=True,
                                  verbose_name='Super tag')


class SuperTagManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_tag__isnull=True)


class SuperTag(Tag):
    objects = SuperTagManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Super tag'
        verbose_name_plural = 'Super tags'


class SubTagManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_tag__isnull=False)


class SubTag(Tag):
    objects = SubTagManager()

    def __str__(self):
        return '%s - %s' % (self.super_tag.name, self.name)

    class Meta:
        proxy = True
        ordering = ('super_tag__order', 'super_tag__name', 'order', 'name')
        verbose_name = 'Sub tag'
        verbose_name_plural = 'Sub tags'


# Gallery Board


class PictureBoard(models.Model):
    tag = models.ForeignKey(SubTag, on_delete=models.PROTECT, verbose_name='Tag')
    title = models.CharField(max_length=40, verbose_name='Picture name')
    description = models.TextField(blank=True, verbose_name='Description')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Picture')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Picture author')
    is_public = models.BooleanField(default=True, db_index=True, verbose_name='Show in gallery?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
        ordering = ['-created_at']


class Comment(models.Model):
    pp = models.ForeignKey(PictureBoard, on_delete=models.CASCADE, verbose_name='Picture post')
    author = models.CharField(max_length=30, verbose_name='Author')
    content = models.TextField(verbose_name='Content')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Show in the screen?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_at']
