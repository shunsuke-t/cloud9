import datetime

#from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_time = models.DateTimeField('date published')
    event_location = models.CharField(max_length=200)
    fee = models.IntegerField()
    #thumbnail = models.ImageField(null=True)
    quota = models.DecimalField(max_digits=3, decimal_places=0)
    pub_date = models.DateTimeField
    
    def __str__(self):
        return self.event_name
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
