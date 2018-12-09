from __future__ import unicode_literals

from django.db import models


class Box(models.Model):

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
