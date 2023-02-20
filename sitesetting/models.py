from django.db import models

class SiteSetting(models.Model):

    text = models.TextField(blank=True, null=True, verbose_name='text')
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='phone_number')
    address = models.TextField(blank=True, null=True, verbose_name='address')
    postal_code = models.IntegerField(blank=True, null=True, verbose_name='postal_code')
    Instagram = models.TextField(blank=True, null=True, verbose_name='Instagram')
    Telegram = models.TextField(blank=True, null=True, verbose_name='Telegram')
    WhatsApp = models.TextField(blank=True, null=True, verbose_name='whatsApp')


class CountPrize(models.Model):

    min_count = models.IntegerField(verbose_name='min_count')
    max_count = models.IntegerField(verbose_name='max_count')
    percentage = models.IntegerField(verbose_name='percentage')
    