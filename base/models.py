from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField()
    department = models.ManyToManyField('Department', blank=True) #blank defines to the system such as serializer

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, null=True)

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    email = models.EmailField()

class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    price = models.FloatField()

class Department(models.Model):
    name = models.CharField(max_length=200)
