from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', verbose_name='User')
    phone_number = models.IntegerField(verbose_name='phone_number')
    Image = models.ImageField(upload_to='profile', blank=True, null=True, verbose_name='Image')
    address = models.TextField(verbose_name='address')
    postal_code = models.IntegerField(verbose_name='postal_code')
    birthday = models.DateField(blank=True, null=True, verbose_name='birthday')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create_date')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='modified_date')

    def __str__(self):
        return self.user.first_name



