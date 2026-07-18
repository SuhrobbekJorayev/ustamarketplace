from django.db.models.signals import post_save
from django.dispatch import receiver
from jobs.models import Order, User, WorkerProfile
from jobs.tasks import send_order_notification_mail


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    print("1. Signal ishga tushdi")

    if not created:
        return

    print("2. created=True")

    worker_user = instance.service.worker
    print("3. Worker:", worker_user.username)
    print("4. Email:", worker_user.email)

    send_order_notification_mail(
        to_email=worker_user.email,
        worker_username=worker_user.username,
        order_id=instance.id,
        client_username=instance.client.username,
        service_name=instance.service.name
    )

    print("5. Email yuborildi")


@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'worker':
        WorkerProfile.objects.create(user=instance)

print("1. Signal ishga tushdi")