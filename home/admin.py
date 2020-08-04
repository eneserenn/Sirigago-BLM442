from django.contrib import admin
from home.models import Setting
from home.models import ContactFormMessage

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status']
    list_filter = ['status']

admin.site.register(Setting,SettingAdmin)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name' , 'status' ,'note']
    list_filter = ['status']

admin.site.register(ContactFormMessage,ContactFormMessageAdmin)