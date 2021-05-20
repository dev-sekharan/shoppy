from django.db import models
from django.utils import timezone
import random

# Create your models here.
class Product(models.Model):
    P_ID = models.AutoField(primary_key=True)
    P_NAME = models.CharField(blank=False, max_length=100)
    P_IMG = models.ImageField(upload_to="products/images")
    P_DESC = models.CharField(blank=False, max_length=1000)
    P_PRICE = models.FloatField(blank=False)
    P_STOCK = models.IntegerField(blank=False)
    STATUS_CHOICES = ((0, 'INACTIVE'), (1,'ACTIVE'))
    P_STATUS = models.IntegerField(choices=STATUS_CHOICES, default=1)
    P_DATE = models.DateTimeField(default = timezone.now) #added date
    P_SLUG = models.SlugField(max_length=40, null=False, unique=True)
