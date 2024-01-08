from rest_framework import serializers 
from .models import Product,Purchase, Stock

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


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True) 


    class Meta:
        model = Stock
        fields = ['product',
                'quantity',
                'unit' ,
                ]
