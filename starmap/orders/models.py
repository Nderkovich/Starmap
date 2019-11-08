from django.db import models
from map_generator.models import Starmap

# Create your models here.
class OrderPdf(models.Model):
    map = models.ForeignKey(Starmap,
                            related_name="orderpdf",
                            on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)


class OrderPic(models.Model):
    map = models.ForeignKey(Starmap,
                            related_name="orderpic",
                            on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    postal_index = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)

