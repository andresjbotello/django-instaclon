#Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Se asegura de que todos los usuarios que esten logueados tengan
        biography y picture """

    def __init__(self, get_response):
        self.get_response = get_response
        # One time configuration and initialization

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')
        
        response = self.get_response(request)
        return response
