from django.contrib import admin
from . models import Product,Cart

admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price','ratings','category','product_image')
    

class CartModelAdmin(admin.ModelAdmin):
    list_display=('id','product','quantity')