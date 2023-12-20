from django.contrib import admin
from .models import Product , Sale , ItenSale , Purchase , Stock


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','color','price_sell')
class StockAdmin(admin.ModelAdmin):
    list_display = ('product','quantity','unit')


     
admin.site.register(Product ,ProductAdmin)
admin.site.register( Stock ,StockAdmin)
admin.site.register(Sale)
admin.site.register(ItenSale)
admin.site.register(Purchase)