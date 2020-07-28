from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task(name='send-mail-task')
def send_mail_task(x, y):
  pass

@shared_task(name='username-validate')
def validate_user(username):
  data = {
      "is_taken": User.objects.filter(username__iexact=username).exists()}
  return data    
