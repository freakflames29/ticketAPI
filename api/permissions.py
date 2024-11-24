from rest_framework.permissions import BasePermission

class Is_Super_Stuff_Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser == True or request.user.is_staff == True or obj.user == request.user:
            return True
        else:
            return False

class Is_Super__Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("*"*100)
        print("obj user",obj.user)
        print("req user",request.user)
        print("*"*100)
        if request.user.is_superuser == True or obj.user == request.user:
            return True
        else:
            return False