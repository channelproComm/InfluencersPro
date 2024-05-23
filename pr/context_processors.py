from Links.models import UserProfile  

def user_package(request):
    user_package = None
    
    # Check if the user is logged in and not a superuser
    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_package = user_profile.package
        except UserProfile.DoesNotExist:
            pass

    return {'user_package': user_package}
