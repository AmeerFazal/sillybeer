from __future__ import unicode_literals

from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.CharField(max_length=2)
   
    def __str__(self):
        return self.name
