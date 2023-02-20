from django.db import models
from django.contrib.auth.models import User


class WholeBuyerUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    Is_WholeBuyer = models.BooleanField(default=False, verbose_name='Is_WholeBuyer')



class SettleMent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    amount = models.IntegerField(verbose_name='amount')
    date = models.DateTimeField(auto_now=True, verbose_name='date')