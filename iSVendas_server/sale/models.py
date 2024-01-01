from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


UNIT_TYPES = (('length','Comprimeto'),
              ('unit','Unidade')
            )
UNIT_ATRS = {UNIT_TYPES[0][0]:{'SIM':('mm','cm','dm','M','dam','hm','Km'),
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
    price = models.FloatField()
    datetime = models.DateTimeField(default = timezone.now)

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete = models.PROTECT)
    quantity = models.FloatField()
    unit = models.CharField(max_length = 2)


@receiver(post_save, sender=Purchase, dispatch_uid="update_stock_count")
def update_stock(sender, instance, **kwargs):
    stock = Stock.objects.get(product=instance.product)
    stock.quantity += unit_covert(instance.product.unit_type,instance.unit,instance.quantity)
    stock.save()
    

def unit_covert(un_type,un,qtd):
    qtd =float(qtd)
    defalt_un = UNIT_ATRS[un_type]['defalt']
    defalt_index = UNIT_ATRS[un_type]['SIM'].index(defalt_un) +1
    un_index = UNIT_ATRS[un_type]['SIM'].index(un) +1 
    pot = (un_index - defalt_index )
    qtd_ = qtd*(10**pot)
    return qtd_

        


