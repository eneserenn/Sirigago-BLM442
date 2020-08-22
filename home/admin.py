from django.contrib import admin
from home.models import Setting
from home.models import ContactFormMessage
from home.models import UserProfile
from home.models import Faq

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status']
    list_filter = ['status']

admin.site.register(Setting,SettingAdmin)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name' , 'status' ,'note']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name' , 'country','phone','address','city','image_tag']


class FaqAdmin(admin.ModelAdmin):
    list_display = ['question','answer','create_at','update_at','status']
    list_filter = ['status']
  

admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Faq,FaqAdmin)