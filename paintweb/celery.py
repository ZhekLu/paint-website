import os

from celery import Celery
from celery.schedules import crontab, crontab_parser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paintweb.settings.production')

app = Celery('paintweb')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'paintsite.tasks.comments_notification',
        # 'schedule': crontab(minute=crontab_parser(60).parse('*/2'))
        'schedule': 60.0
    }

}
app.autodiscover_tasks()
