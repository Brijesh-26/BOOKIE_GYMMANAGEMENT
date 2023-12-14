from rest_framework import permissions

class IsTrainerForWorkoutSession(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read only permission to all request
        if request.method in permissions.SAFE_METHODS:
            return True

        # checking if workout trainer is equal to request.user(if it is trainer)
        return obj.trainer == request.user.trainer 
    
    
# For checking above permission we'll have to create a separate user model then only we can check 
# our permission on postman
# BUT THERE IS NO MENTION OF ANY USER MODEL IN THE ASSIGNMENT, SO I'VE NOT CREATED ANY
# SEPARATE MODEL FROM MY SIDE BUT I'VE ADDED ALL THE GIVEN PERMISSION.

