from django.db import models
from django.utils import timezone


UNIT_TYPES = (('length','Comprimeto'),
              ('unit','Unidade')
            )
UNIT_ATRS = {UNIT_TYPES[0][0]:{'SIM':('mm','cm','M','Km'),
                                'defalt':'M'
                              },
            UNIT_TYPES[1][0]:{'SIM':('UN'),
            'defalt':'UN'
            }
            }

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    description =  models.CharField(max_length=250)
    color =  models.CharField(max_length=20)
    suplayer =  models.CharField(max_length=250)
    wifi = models.BooleanField()
    zegbee = models.BooleanField()
    rf =  models.BooleanField()
    attrs = models.JSONField()
    unit_type = models.CharField(max_length=100, choices=UNIT_TYPES)
    barcode = models.CharField(max_length=50, null=True, blank=True)
    price_sell = models.FloatField()

class Sale(models.Model):
    client = models.CharField(max_length=250)
    total_price = models.FloatField()
    datetime = models.DateTimeField(default = timezone.now)

class ItenSale(models.Model):
    product = models.ForeignKey(Product,on_delete= models.PROTECT)
    sale = models.ForeignKey(Sale,on_delete= models.PROTECT)
    quantity = models.FloatField()
    unit  =  models.CharField(max_length=2)
    price_sold = models.FloatField()

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete= models.PROTECT)
    quantity = models.FloatField()
    unit  =  models.CharField(max_length=2)
    datetime = models.DateTimeField(default = timezone.now)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.FloatField()
    unit = models.CharField(max_length = 2)