from django.db.models.signals import post_save
from django.dispatch import receiver

from jobs.models import Order
from jobs.tasks import send_order_notification_mail


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if not created:
        return

    worker_user = instance.service.worker.user

    send_order_notification_mail.delay(
        to_email=worker_user.email,
        worker_username=worker_user.username,
        order_id=instance.id,
        client_username=instance.client.username,
        service_name=instance.service.name
    )
# email completed, now give it a try
