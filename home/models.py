from django.db import models
from django.utils import timezone


class VisitorData(models.Model):
    ip = models.CharField(max_length=20, blank=True, null=True, default='')
    objects = None



