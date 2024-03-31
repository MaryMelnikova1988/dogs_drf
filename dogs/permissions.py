from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        if request.user.roles == UserRoles.MODERATOR:
            return True
        return False

    # решение с лайва / группа создавалась через админку/
    # def has_permission(self, request, view):
    #     return request.user.groups.filter(name='moderator').exists()


class IsDogOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False

        # решение с лайва
        # def has_object_permission(self, request, view, obj):
        #     if request.user == obj.user:
        #         return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
        #     return False


class IsDogPublic(BasePermission):
    message = "Собака не является публичной"

    def has_object_permission(self, request, view, obj):
        return obj.is_public
