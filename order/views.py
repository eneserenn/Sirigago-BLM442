from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hotel.models import Product

# Create your views here.
from order.models import Reservation,ReservationForm
from hotel.models import Category

def index(request):
    return HttpResponse("Order APP")

@login_required(login_url='/login')
def Reserve(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        print ("HATALAR")
        print (form.errors)
        if form.is_valid():
            current_user = request.user

            data = Reservation()
            data.user_id = current_user.id
            data.product_id = id
            data.check_in = form.cleaned_data['check_in']
            data.check_out = form.cleaned_data['check_out']
            data.kisisayisi = form.cleaned_data['kisisayisi']
            product= Product.objects.get(pk=id)
            kalanoda= product.odasayisi
            toplam_odeme = data.kisisayisi * product.price
            data.price = toplam_odeme
            if kalanoda > 0:
             for db in Reservation.objects.all():
                if db.product_id == data.product_id and db.check_in >= data.check_in and db.check_out <= data.check_out:
                    return HttpResponse("Bu Tarih aralığı dolu")
                else:
                    data.save()
                    t=Product.objects.get(id=data.product_id)
                    kalanoda=kalanoda-1
                    t.odasayisi=kalanoda
                    t.save()
                    messages.success(request, "Rezervasyonlarımdan rezervasyonunuzu kontrol edebilirsiniz.İşlem Başarılı")
                    return HttpResponseRedirect(url)
                    
            else:
                
                    messages.warning(request, "Boş odamız Kalmamıştır")
                 
              
           
        else:
            messages.error(request,"Hata VAR")
    return HttpResponseRedirect(url)
        
