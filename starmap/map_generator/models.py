from django.db import models
from .choices import *

# Create your models here.
class Starmap(models.Model):
    date = models.DateField()
    text = models.TextField(max_length=400)
    city = models.CharField(max_length=250)
    map_type = models.IntegerField(choices=MAP_TYPE_CHOICES, default=1)