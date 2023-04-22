from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Product(models.Model):
    plant_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.plant_type

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
