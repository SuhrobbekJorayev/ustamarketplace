from django.contrib import admin
from jobs.models import Category, Order, Review, Service, User, WorkerProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(WorkerProfile)
