from django.db import models
from django.contrib.auth.models import User


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
