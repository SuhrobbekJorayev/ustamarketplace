# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from jobs.models import Order
# from jobs.tasks import send_order_notification_mail
#
#
# @receiver(post_save, sender=Order)
# def order_created(sender, instance, created, **kwargs):
#     if not created:
#         return
#
#     worker_user = instance.service.worker
#
#     send_order_notification_mail(
#         to_email=worker_user.email,
#         worker_username=worker_user.username,
#         order_id=instance.id,
#         client_username=instance.client.username,
#         service_name=instance.service.name
#     )
# # email completed, now give it a try

from django.db.models.signals import post_save
from django.dispatch import receiver
from jobs.models import User, WorkerProfile


@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'worker':
        WorkerProfile.objects.create(user=instance)
