from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput
from hotel.models import Product
from django.utils import timezone

# Create your models here.

# class ShopCart(models.Model):
#     availible=models.IntegerField()
#     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
#     product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
#     quantity = models.IntegerField()

    
#     def __str__(self):
#         return self.product.title
    
#     @property
#     def amount(self):
#         return(self.quantity * self.product.price)
#     @property
#     def price(self):
#         return(self.product.price)

# class ShopCartForm(ModelForm):
#     class Meta:
#         model=ShopCart
#         fields = ['quantity']


class Reservation(models.Model):
    STATUS = (
        ('Onaylandı','Onaylandı'),
        ('Beklemede','Beklemede'),
        ('Reddedildi','Reddedildi'),
    )
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    kisisayisi=models.IntegerField(blank=False)
    price=models.IntegerField(blank=False)
    status=models.CharField(max_length=10 , choices=STATUS, default="Beklemede")

    def dondur(self):
        return self.kisisayisi,self.check_in,self.check_out,self.price
    
        


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in','check_out','kisisayisi']
    
    
