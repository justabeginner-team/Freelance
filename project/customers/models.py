from django.db import models
# from ..retailers.models import Product


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=500, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    # product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name
