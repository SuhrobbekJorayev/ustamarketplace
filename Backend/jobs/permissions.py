from rest_framework import permissions


class IsClient(permissions.BasePermission):
    """Allow access only to authenticated clients."""

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.user.role == 'client'
        )


class IsOrderParticipant(permissions.BasePermission):
    """Allow access only to the order client or service owner."""

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in permissions.SAFE_METHODS:
            return obj.client == user or (obj.service and obj.service.worker == user)

        new_status = request.data.get('status')

        if obj.client == user:
            if obj.status == 'pending' and new_status == 'canceled':
                return True
            return False

        if obj.service and obj.service.worker == user:
            if new_status in ('accepted', 'completed', 'canceled'):
                return True
            return False

        return False


class IsWorker(permissions.BasePermission):
    """Allow access only to authenticated workers."""

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.user.role == 'worker'
        )


class IsServiceOwner(permissions.BasePermission):
    """Allow only the service owner to modify the service."""

    def has_object_permission(self, request, view, obj):
        return obj.worker == request.user


class IsReviewOwner(permissions.BasePermission):
    """Allow only the review owner to modify the review"""

    def has_object_permission(self, request, view, obj):
        return obj.order.client == request.user
