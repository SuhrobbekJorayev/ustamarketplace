from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs.views import (
    CategoryViewSet,
    ServiceViewSet,
    OrderViewSet,
    ReviewViewSet,
    WorkerProfileView,
    WorkerPublicViewSet,
    MeView
)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'worker-public', WorkerPublicViewSet)

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
    path("worker-profile/", WorkerProfileView.as_view(), name="worker-profile"),

    path('', include(router.urls))
]
