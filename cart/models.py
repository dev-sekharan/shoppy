from django.db import models
from product.models import Product
from django.conf import settings

# Create your models here.


class Cart(models.Model):
    U_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=None)
    P_ID = models.ForeignKey(Product, on_delete=models.CASCADE, blank=None)
    C_QTY = models.IntegerField(default=1, null=None)
    C_DATE = models.DateTimeField(auto_now=True)

