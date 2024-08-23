import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djang_celery.settings")
app = Celery("Djang_Celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
