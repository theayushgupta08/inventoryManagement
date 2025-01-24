from django.contrib import admin
from .models import Product, Supplier, SaleOrder, StockMovement

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(SaleOrder)
admin.site.register(StockMovement)