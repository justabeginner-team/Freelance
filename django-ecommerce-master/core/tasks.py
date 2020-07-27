from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task(name='send-mail-task')
def send_mail_task(x, y):
  pass
