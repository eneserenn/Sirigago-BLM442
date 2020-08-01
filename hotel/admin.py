from django.contrib import admin

# Register your models here.
from hotel.models import Category
from hotel.models import Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status','category', 'price']
    list_filter = ['price','star']

admin.site.register(Product,ProductAdmin)