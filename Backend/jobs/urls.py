from rest_framework.routers import DefaultRouter
from jobs.views import (
    CategoryViewSet,
    ServiceViewSet,
    OrderViewSet,
    ReviewViewSet,
    # WorkerProfileViewSet,
    # UserViewSet
)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
# router.register(r'worker-profiles', WorkerProfileViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = router.urls
