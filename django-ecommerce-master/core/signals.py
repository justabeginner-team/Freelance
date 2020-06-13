# from django.db.models.signals import post_save
# from .models import UserProfile
# from django.conf import settings
#
#
# def userprofile_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         userprofile = UserProfile.objects.create(user=instance)
#         print('user created')
#
#
# post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
