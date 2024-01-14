from rest_framework import permissions

class IsDevPermission(permissions.DjangoModelPermissions):
    '''
    Custom Permission
    '''
    def has_permission(self, request, view):
        if not request.user.is_dev:
            return False
        return super().has_permission(request, view)
