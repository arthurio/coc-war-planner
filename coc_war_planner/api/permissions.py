from rest_framework import permissions


class IsChiefOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.chief == request.user.member


class IsNotPartOfClanOrCreateNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return (request.user.member.clan is None
                    and not request.user.member.is_chief())

        return True


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.member.user == request.user


class CreateNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return False

        return True

