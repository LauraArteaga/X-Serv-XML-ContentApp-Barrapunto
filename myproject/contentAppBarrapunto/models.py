from django.db import models

# Create your models here.

class Resource(models.Model):
    key = models.CharField(max_length = 20)
    value = models.IntegerField()
