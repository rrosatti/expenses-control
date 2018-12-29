from django.contrib import admin
from .models import Expense, UserCustom


class ExpenseAdmin(admin.ModelAdmin):
    model = Expense

    list_display = (
        'id', 'value', 'date', 'short_desc',
        'long_desc', 'get_user')

    verbose_name = "Expenses List"

    def get_user(self, obj):
        return obj.user.username

    get_user.short_description = 'User'


class UserCustomAdmin(admin.ModelAdmin):
    model = UserCustom

    list_display = ('get_user', 'max_value', 'send_notifications')

    verbose_name = 'Users Expense List'

    def get_user(self, obj):
        return obj.user.username

    get_user.short_description = 'User'


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(UserCustom, UserCustomAdmin)
