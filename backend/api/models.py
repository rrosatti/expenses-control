from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(_("Date"), default=datetime.date.today)
    short_desc = models.CharField(max_length=40)
    long_desc = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s/%s/%s - $ %s (%s)" % \
            (self.date__year, self.date__month,
                self.date__day, self.value, self.short_desc)

    class Meta:
        ordering = ('-date__year', '-date__month', '-date__day',)


class UserCustom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    max_value = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal('0.00'))
    send_notifications = models.BooleanField(default=False)

    def __str__(self):
        return "%s: \nMax Value: %s | Send Notifications: %s" % \
            (self.user__username, self.max_value, self.send_notifications)
