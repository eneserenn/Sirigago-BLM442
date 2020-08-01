from django.contrib import admin

# Register your models here.
from hotel.models import Category
from hotel.models import Product
from hotel.models import Images

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status','category', 'price','image_tag']
    list_filter = ['price','star']
    inlines = [ImagesInline]

admin.site.register(Product,ProductAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','hotel','image_tag']
   

admin.site.register(Images,ImagesAdmin)