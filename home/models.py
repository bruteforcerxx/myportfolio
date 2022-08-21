from django.db import models
from django.utils import timezone


class VisitorData(models.Model):
    ip = models.CharField(max_length=20, blank=True, null=True, default='')
    latlng = models.CharField(max_length=20, blank=True, null=True, default='')
    sn = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0.0)
    objects = None



