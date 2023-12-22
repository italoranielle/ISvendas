from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 
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

# ViewSets define the view behavior.






