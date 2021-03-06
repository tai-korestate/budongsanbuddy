from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

outer = "unknown"

class Properties(models.Model):

    db_user = outer

    account_ref = models.CharField(max_length = 64)

    post_date = models.DateTimeField("Date Posted", auto_now_add = True)
    last_edit = models.DateTimeField("Last Edited", auto_now = True)
    pics = models.FileField(upload_to = db_user)
    pics2 = models.FileField(upload_to = db_user)
    pics3 = models.FileField(upload_to = db_user)
    description = models.CharField(max_length = 255)
    broker_name = models.CharField(max_length = 15)
    property_name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 15)
    radio_array = models.CharField(max_length = 255)  
  
    class Meta:
        unique_together = ["pics","description","broker_name","property_name","phone_number"]

    def was_published_recently(self): #Boilerplate django from polls
        now = timezone.now()
        past = timezone.now() - datetime.timedelta(days = 1)
        return now >= self.pub_date >= past


    def __str__(self):
        return str(self.account_ref) +'::'+ str(self.broker_name)+'::'+ str(self.post_date)
