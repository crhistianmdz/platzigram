from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('login/',views.login_view, name='login_view' ),
    path('logout/',views.logout_view, name='logout_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('me/profile/',views.update_profile_view, name='update_profile_view'),
    path('<str:username>/',views.UserDetailView.as_view(),name='detail')
]
