from django.db import models

# Create your models here.
class LogisticInfo(models.Model):

    distance = models.FloatField(default=0, blank=False)
    type_delivery = models.CharField(max_length=10, blank=False)
    masa = models.FloatField(default=0, blank=False)
    pib = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=13, blank=False)
    email = models.EmailField(max_length=30,blank=False)