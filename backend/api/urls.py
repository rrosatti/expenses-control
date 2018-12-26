from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUser, LogoutUser, CreateUserCustom, \
    UserCustomViewSet, ExpenseViewSet


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
    url(r'^expenses/create/$',
        ExpenseViewSet.as_view({'post': 'create'}),
        name='expenses_create_expense'),
    url(r'^expenses/$',
        ExpenseViewSet.as_view({'get': 'list'}),
        name='expenses_list_expenses'),
    url(r'^expenses/(?P<expense_id>[0-9]+)/$',
        ExpenseViewSet.as_view({'get': 'retrieve'}),
        name='expenses_get_expense'),
    url(r'^custom/create/$',
        CreateUserCustom.as_view(),
        name='custom_create'),
    url(r'^custom/$',
        UserCustomViewSet.as_view({'get': 'retrieve'}),
        name='custom_get'),
]
