from __future__ import unicode_literals

from django.db import models


class Motor(models.Model):
    fuel = models.DecimalField(max_digits=3, decimal_places=2, default=0, null=False, blank=False, help_text='Gasoline iha motor')
    engine_size = models.DecimalField(max_digits=3, decimal_places=0, default=125, null=False, blank=False, help_text='Size of engine ( cc )')
    model = models.CharField(max_length=16, null=False, blank=False, help_text='Model name')
    photo = models.ImageField(help_text='Picture of motor', null=True, blank=True)
