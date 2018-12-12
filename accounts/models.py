from __future__ import unicode_literals

from urllib import request

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Box(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='boxs2', blank=True)
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    number = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    image = models.FileField()
    wiegth = models.IntegerField()

    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __unicode__(self):
        return self.From
