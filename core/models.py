from django.contrib.auth.models import User
from django.db import models


class Sales(models.Model):
    salesman = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    number = models.IntegerField()
    approve_order = models.BooleanField(default=False)

    def __str__(self):
        return self.salesman

    class Meta:
        verbose_name_plural = 'Sales'


class Administration(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    account = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.administrator

    class Meta:
        verbose_name_plural = 'Administrators'
