from allauth.account.signals import email_confirmed
from allauth.account.models import EmailAddress
from django.db.models.signals import post_save, pre_save

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


# @receiver(pre_save, sender=Item)
# def item_receiver(sender, instance, *args, **kwargs):
#     Item.objects.create(user=instance)
#     print('item created')


@receiver(email_confirmed)
def update_user_email(sender, request, email_address, **kwargs):
    # Once the email address is confirmed, make new email_address primary.
    # This also sets user.email to the new email address.
    # email_address is an instance of allauth.account.models.EmailAddress
    email_address.set_as_primary()
    # Get rid of old email addresses
    stale_addresses = EmailAddress.objects.filter(
        user=email_address.user).exclude(primary=True).delete()
