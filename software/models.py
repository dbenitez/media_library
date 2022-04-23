from pyexpat import model
from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=128)
    website = models.URLField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

class ProductType(models.Model):
    name = models.CharField(max_length=16)

class ProductPlatform(models.Model):
    name = models.CharField(max_length=16)

class ProductCPU(models.Model):
    name = models.CharField(max_length=16)
    display_order = models.PositiveSmallIntegerField()

class ProductUI(models.Model):
    name = models.CharField(max_length=16)

class ProductVersion(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    name = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    serials = models.TextField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField(null=True, blank=True)
    end_of_life_date = models.DateField(null=True, blank=True)
    min_cpu = models.ForeignKey(ProductCPU, on_delete=models.SET_NULL, null=True)
    min_ram = models.PositiveSmallIntegerField(null=True, blank=True)
    min_hd = models.PositiveSmallIntegerField(null=True, blank=True)
    ui = models.ForeignKey(ProductUI, on_delete=models.SET_NULL, null=True)
    platforms = models.ManyToManyField(ProductPlatform, blank=True)
    types = models.ManyToManyField(ProductType, blank=True)

