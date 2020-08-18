from django.http import HttpResponse
from hotel.models import CommentForm , Comments
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("Hotels Page")

@login_required(login_url='/login')
def addcomment(request,id):
    
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data = Comments()
            data.user_id= current_user.id
            data.product_id = id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"yorum başarılı bir şekilde gonderildi")
            
            return HttpResponseRedirect(url)
    messages.error(request,"Hata VAR")
    return HttpResponseRedirect(url)
