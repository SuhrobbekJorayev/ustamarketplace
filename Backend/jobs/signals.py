import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from jobs.models import Order, User, WorkerProfile
from jobs.tasks import send_order_notification_mail


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if not created:
        return

    worker_user = instance.service.worker

    threading.Thread(
        target=send_order_notification_mail,
        args=(
            worker_user.email,
            worker_user.username,
            instance.id,
            instance.client.username,
            instance.service.name
        ),
        daemon=True
    ).start()


@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'worker':
        WorkerProfile.objects.create(user=instance)
