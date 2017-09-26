from django.db import models
from django.utils import timezone
# Create your models here.


class MaritalStatus(models.Model):
    marital = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150,blank=True, null=True)
    def __str__(self):
        return self.marital

class PreRegister(models.Model):
    cpf_cnpj = models.CharField(max_length=14, null = False, unique=True)
    name = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.name

class Insured(models.Model):
    cpf_cnpj = models.CharField(max_length=14, null = False)
    name = models.CharField(max_length=50, null=False)
    born_date = models.DateTimeField(null=False)
    rg = models.CharField(max_length=10, null = False)
    org_exp = models.CharField(max_length=10, null = False)
    exp_date = models.DateTimeField(null=False)
    ppe = models.BooleanField(default=False)
    marital_status = models.ForeignKey('cotador.MaritalStatus')
    def __str__(self):
        return self.name



class Quotation(models.Model):
    protocol = models.CharField(max_length=10, null=False)
    client = models.ForeignKey('cotador.PreRegister')
    product = models.ForeignKey('cotador.Product')
    uf = models.ForeignKey('cotador.Uf')
    city = models.ForeignKey('cotador.City')
    lvl_cob = models.ForeignKey('cotador.Lvl_Cob')
    area = models.FloatField(null=False)
    sack_price = models.FloatField(null=False)
    prod_esp =  models.FloatField(null=False)
    prod_seg =  models.FloatField(null=False)
    total_is =  models.FloatField(null=False)
    total_cost =  models.FloatField(null=False)
    subv_fed =  models.FloatField(null=False)
    subv_est =  models.FloatField(null=False)
    final_cost =  models.FloatField(null=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        quot_inf = str(self.protocol) + " - " + str(self.client)
        return quot_inf


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
    product = models.ForeignKey('cotador.Product')
    def __str__(self):
        return self.name


class Tax(models.Model):
    product = models.ForeignKey('cotador.Product')
    city = models.ForeignKey('cotador.City')

    nc_60 = models.FloatField()
    nc_65 = models.FloatField()
    nc_70 = models.FloatField()
    active = models.BooleanField(default=False)

    def __str__(self):
        tax_inf = str(self.product) + " - " + str(self.city)
        return tax_inf

class Lvl_Cob(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
