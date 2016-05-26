from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Properties(models.Model):

    account_ref = models.CharField(max_length = 64)

    post_date = models.DateTimeField("Date Posted", auto_now_add = True)
    last_edit = models.DateTimeField("Last Edited", auto_now = True)
    pics = models.FileField(upload_to = 'testdir')
    description = models.CharField(max_length = 255)
    broker_name = models.CharField(max_length = 15)
    property_name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 15)
    class Meta:
        unique_together = ["pics","description","broker_name","property_name","phone_number"]

    def was_published_recently(self): #Boilerplate django from polls
        now = timezone.now()
        past = timezone.now() - datetime.timedelta(days = 1)
        return now >= self.pub_date >= past


    def __str__(self):
        return str(self.post_date)
