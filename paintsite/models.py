from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Was activated?')
    send_messages = models.BooleanField(default=True, verbose_name='Want to get messages about new comments?')

    class Meta(AbstractUser.Meta):
        pass


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
