from rest_framework import permissions


class IsQuizAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool((request.user.role == 'Quiz author'))


class IsPlayer(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool((request.user.role == 'Player'))



