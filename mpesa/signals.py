from celery import chain
from .tasks import (
    call_online_checkout_task,
    handle_online_checkout_response_task,
)
from django.dispatch import receiver
from .models import  OnlineCheckout
from django.db.models.signals import post_save




@receiver(post_save, sender=OnlineCheckout)
def handle_online_checkout_post_save(sender, instance, **Kwargs):
    """
    Handle online checkout post save
    :param sender:
    :param instance:
    :param Kwargs:
    :return:
    """

    # online checkout
    chain(
        call_online_checkout_task.s(
            instance.phone,
            int(instance.amount),
            instance.account_reference,
            instance.transaction_description,
            instance.is_paybill,
        ),
        handle_online_checkout_response_task.s(instance.id),
    ).apply_async(queue="online_checkout_request")
