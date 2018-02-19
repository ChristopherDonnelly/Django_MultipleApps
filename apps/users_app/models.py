# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "\n\tID: {}\n\tFirst Name: {}\n\tLast Name: {}\n\tEmail: {}\n\tAge: {}\n".format(str(self.id), str(self.first_name), str(self.last_name), str(self.email), str(self.age))