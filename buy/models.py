from django.db import models
from product.models import Product
from django.conf import settings

# Create your models here.


class Buy(models.Model):
    B_USER = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=None)
    B_PRODUCT = models.ForeignKey(Product, on_delete=models.CASCADE, blank=None)
    B_QUANTITY = models.IntegerField(default=1, null=None)
    B_PRICE = models.FloatField(null=None)
    STATUS_CHOICES = ((0, 'ORDERED'), (1, 'SHIPPED'),(2, 'DELIVERED'))
    B_STATUS = models.IntegerField(choices=STATUS_CHOICES, default=0)
    B_DATE = models.DateTimeField(auto_now=True)
