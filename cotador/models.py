from django.db import models
from django.utils import timezone
# Create your models here.

class Uf(models.Model):
    sigla = models.CharField(max_length=2, null=False)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    uf = models.ForeignKey('cotador.Uf')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Safra(models.Model):
    culture = models.ForeignKey('cotador.Culture')
    safra_inf = models.CharField(max_length=50)
    safra_begin = models.DateTimeField(
            blank=True, null=True)
    safra_end = models.DateTimeField(
            blank=True, null=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.safra_inf


class Product(models.Model):
    name = models.CharField(max_length=50)
    safra = models.ForeignKey('cotador.Safra')
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Prod_Esp(models.Model):
    product = models.ForeignKey('cotador.Product')
    city = models.ForeignKey('cotador.City')
    value = models.FloatField()

    def __str__(self):
        return self.city.name

class Culture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tax(models.Model):
    product = models.ForeignKey('cotador.Product')
    city = models.ForeignKey('cotador.City')
    tax_inf = product.name + " - " + city.name
    nc_60 = models.FloatField()
    nc_65 = models.FloatField()
    nc_70 = models.FloatField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.tax_inf

class Lvl_Cob(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
