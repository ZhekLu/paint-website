from django.contrib import admin
import datetime

from .forms import SubTagForm
from .models import User, SubTag, SuperTag, PictureBoard
from .utilities import send_activation_notification


def send_activation_notifications(model_admin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    model_admin.message_user(request, 'Emails with requirements were sent')


send_activation_notifications.short_description = 'Sending activation mails'


class NotActivatedFilter(admin.SimpleListFilter):
    title = 'Was activated?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'has been activated'),
            ('three days', 'has not been activated within three days'),
            ('week', 'has not been activated for more than a week')
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'three days':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)


class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NotActivatedFilter, )
    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('send_messages', 'is_active', 'is_activated'),
        ('is_staff', 'is_superuser'),
        'groups', 'user_permissions',
        ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications, )


admin.site.register(User, UserAdmin)


class SubTagInline(admin.TabularInline):
    model = SubTag


class SuperTagAdmin(admin.ModelAdmin):
    exclude = ('super_tag', )
    inlines = (SubTagInline, )


admin.site.register(SuperTag, SuperTagAdmin)


class SubTagAdmin(admin.ModelAdmin):
    form = SubTagForm


admin.site.register(SubTag, SubTagAdmin)


class PictureBoardAdmin(admin.ModelAdmin):
    list_display = ('tag', 'title', 'description', 'author', 'created_at')
    fields = (
        ('tag', 'author'),
        'title', 'description',
        'image',
        'is_public'
    )


admin.site.register(PictureBoard, PictureBoardAdmin)
