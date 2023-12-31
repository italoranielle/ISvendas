from rest_framework import serializers 
from .models import Product,Purchase

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['pk',
            'name', 
            'description', 
            'color', 
            'suplayer', 
            'wifi', 
            'zegbee', 
            'rf', 
            'attrs',
            'unit_type',
            'barcode',
            'price_sell']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['product',
                'quantity',
                'unit' ,
                'price',
                'datetime']



