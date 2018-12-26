from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUser, LogoutUser, CreateExpense, ExpenseList,\
    ExpenseDetail, CreateUserCustom, UserCustomViewSet


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
        CreateExpense.as_view(),
        name='expenses_create_expense'),
    url(r'^expenses/$',
        ExpenseList.as_view(),
        name='expenses_list_expenses'),
    url(r'^expenses/(?P<expense_id>[0-9]+)/$',
        ExpenseDetail.as_view(),
        name='expenses_get_expense'),
    url(r'^custom/create/$',
        CreateUserCustom.as_view(),
        name='custom_create'),
    url(r'^custom/$',
        UserCustomViewSet.as_view({'get': 'retrieve'}),
        name='custom_get'),
]
