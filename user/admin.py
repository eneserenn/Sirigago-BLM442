from django.contrib import admin
from order.models import Reservation

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['check_in','check_out','kisisayisi','price','status']
    list_filter = ['status']

admin.site.register(Reservation,OrderAdmin)