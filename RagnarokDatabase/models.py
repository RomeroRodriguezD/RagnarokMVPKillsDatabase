from django.db import models
import pandas as pd
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

# ORM

class MVP(models.Model):  
    name= models.CharField(max_length=128)

    def __str__(self):
        '''String for representing the Model Object'''
        return self.name

class Kills(models.Model):
    CHOICES = []
    listmvp = pd.read_csv('RagnarokDatabase/static/Lista MVP.csv')
    for row in listmvp.itertuples():
        CHOICES.append(row)

    name= models.CharField(max_length=128)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        '''String for representing the Model Object'''
        return self.name
