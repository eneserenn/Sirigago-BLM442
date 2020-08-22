from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from hotel.models import Category
from home.models import UserProfile
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from home.models import UserProfile
from user.forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from order.models import Reservation
from hotel.models import Product
from hotel.models import Comments

# Create your views here.
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
                'category': category,
                'profile': profile
            }
    return render(request,'user_profile.html',context)

def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Hesap Güncellendi')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request,'user_update.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your Password was succesfuly updated')
        else:
            messages.error(request,'Please correct yhe errow below')
    else:
        category= Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request,'change_password.html',{
            'form':form,
            'category': category
        })
@login_required(login_url='/login')
def orders(request):
    category= Category.objects.all()
    current_user=request.user
    orders=Reservation.objects.filter(user_id=current_user.id)
    
    context = {
            'category': category,
            'orders': orders,
        }

    return render(request,'user_orders.html',context)

@login_required(login_url='/login')
def mycomment(request):
    category= Category.objects.all()
    current_user=request.user
    comments=Comments.objects.filter(user_id=current_user.id)
    
    context = {
            'category': category,
            'comments': comments,
        }

    return render(request,'my_comments.html',context)

@login_required(login_url='/login')
def orderdelete(request,id):
    url = request.META.get('HTTP_REFERER')
    category= Category.objects.all()
    current_user=request.user
    orders=Reservation.objects.filter(id=id).delete()
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def commentdelete(request,id):
    url = request.META.get('HTTP_REFERER')
    category= Category.objects.all()
    current_user=request.user
    orders=Comments.objects.filter(id=id).delete()
    return HttpResponseRedirect(url)
