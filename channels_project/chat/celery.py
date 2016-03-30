from celery import Celery

import settings
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')
app = Celery('chat')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
