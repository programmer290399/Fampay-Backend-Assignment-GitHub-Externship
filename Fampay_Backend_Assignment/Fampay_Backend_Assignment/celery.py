import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Fampay_Backend_Assignment.settings")

app = Celery("Fampay_Backend_Assignment")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@app.task(bind=True)
def hello_world(self):
    print("Hello world!")
