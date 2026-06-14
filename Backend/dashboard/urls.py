from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard.views import (
    AdminCategoryViewSet,
    AdminUserViewSet,
    AdminWorkerProfileViewSet,
    AdminServiceViewSet,
    AdminOrderViewSet,
    AdminReviewViewSet,
    AdminDashboardStatsView
)


router = DefaultRouter()
router.register(r'categories', AdminCategoryViewSet, basename='admin-categories')
router.register(r'users', AdminUserViewSet, basename='admin-users')
router.register(r'worker-profiles', AdminWorkerProfileViewSet, basename='admin-worker-profiles')
router.register(r'services', AdminServiceViewSet, basename='admin-services')
router.register(r'orders', AdminOrderViewSet, basename='admin-orders')
router.register(r'reviews', AdminReviewViewSet, basename='admin-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', AdminDashboardStatsView.as_view(), name='dashboard-stats'),
]
