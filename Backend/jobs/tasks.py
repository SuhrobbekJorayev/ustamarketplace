from django.core.mail import send_mail
from django.conf import settings


def send_order_notification_mail(to_email, worker_username, order_id, client_username, service_name):
    send_mail(
        subject='Sizga yangi buyurtma keldi',
        message=f"""
Salom {worker_username}!

Sizga yangi buyurtma biriktirildi.

Buyurtma ID: {order_id}
Mijoz: {client_username}
Xizmat: {service_name}

Platformaga kirib buyurtma tafsilotlarini ko'rishingiz mumkin.

Hurmat bilan,
UstaMarketplace
""",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['jsrealm.web@gmail.com'],
        fail_silently=False
    )
