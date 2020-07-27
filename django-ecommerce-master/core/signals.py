# from django.db.models.signals import post_save
from django.db.models.signals import post_save

from .models import LoggedInUser, Item
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver


@receiver(user_logged_in)
def on_user_logged_in(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()

# def userprofile_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         userprofile = UserProfile.objects.create(user=instance)
#         print('user created')
#
#
# post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


# def item_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         Item.objects.create(user=instance)
#
#  post_save.connect(item_receiver, sender=Item)
