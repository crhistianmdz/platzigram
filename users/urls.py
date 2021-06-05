from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_view, name='login_view' ),
    path('logout/',views.logout_view, name='logout_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('me/profile/',views.update_profile_view, name='update_profile_view'),
]
