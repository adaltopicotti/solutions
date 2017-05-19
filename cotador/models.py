from django.db import models
from django.utils import timezone
# Create your models here.

class City(models.Model):
    #uf = models.ForeignKey('uf.name')
    city_name = models.CharField(max_length=50)
