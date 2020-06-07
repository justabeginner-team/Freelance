from django.db import models


# Create your models here.
class Retailer(models.Model):
    name = models.CharField(max_length=500, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=500, null=True)
    picture = models.ImageField(blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
