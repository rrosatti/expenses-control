from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUser, LogoutUser


urlpatterns = [
    url(r'^auth/login/$',
        obtain_auth_token,
        name='auth_user_login'),
    url(r'^auth/register/$',
        CreateUser.as_view(),
        name='auth_user_create'),
    url(r'^auth/logout/$',
        LogoutUser.as_view(),
        name='auth_user_logout'),
]
