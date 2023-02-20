from django.db import models
from customaccount.models import User


class Section(models.Model):
    name = models.CharField(max_length=999, verbose_name='name')
    slug = models.CharField(max_length=999, verbose_name='slug')


class Ticket(models.Model):
    title = models.CharField(max_length=999, verbose_name='title')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='section')
    text = models.TextField(verbose_name='text')
    attachment = models.FileField(upload_to='ticket', blank=True, null=True, verbose_name='attachment')
    code = models.IntegerField(unique=True, blank=True, null=True, verbose_name='code')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create_date')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='modified_date')
    closed = models.BooleanField(default=False, verbose_name='closed')


class TicketMessages(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='TicketMessage', on_delete=models.CASCADE, verbose_name='ticket')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create_date')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='modified_date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    text = models.TextField(verbose_name='text')
    attachment = models.FileField(upload_to='ticket', blank=True, null=True, verbose_name='attachment')
