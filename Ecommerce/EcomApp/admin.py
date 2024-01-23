from django.contrib import admin
from .models import Product,CartItem,Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','price','image']

admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','user']

admin.site.register(CartItem,CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','id','quantity','user','is_completed']

admin.site.register(Order,OrderAdmin)