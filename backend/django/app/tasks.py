from mysite.celery import app as celery_app
from celery import shared_task


@celery_app.task
def hello():
    print('Hello celery!')


@shared_task
def work():
    print('Hello work!')
