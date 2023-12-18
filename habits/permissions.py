from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """Проверка на владельца"""
    message = 'Вы не являетесь владельцем'

    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
        return False
