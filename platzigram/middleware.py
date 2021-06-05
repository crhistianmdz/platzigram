#django
from django.contrib.auth import logout
from users.views import update_profile_view
from django.http import response
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    # ensure everu user that is interaction with the platform have their profile picture and byography

    def __init__(self,get_response):
        #middleware initialization
        self.get_response=get_response

    def __call__(self,request):
        #code to ve executed for each request before the view is called
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile=request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile_view'), reverse('logout_view')]:
                        return redirect('update_profile_view')

        response = self.get_response(request)
        return response
