from django.db import models

class NewsEmails(models.Model):
    Email = models.EmailField(verbose_name='Email')


class NewsLetterMessage(models.Model):
    subject = models.CharField(max_length=999, verbose_name="Subject")
    body = models.TextField(verbose_name="Body")
    attachment = models.FileField(upload_to="Newsletter", verbose_name="Attachment", blank=True)
    publish = models.BooleanField(default=False, verbose_name="Draft")
