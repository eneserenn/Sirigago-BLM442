from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactFormMessage, ContactFormu
from django.contrib import messages
from hotel.models import Product
from hotel.models import Category
from hotel.models import Comments
from hotel.models import Images
from home.forms import SearchForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from home.forms import SignUpForm
from home.models import UserProfile
# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()
    fourludata = Product.objects.all().order_by('?')[1:5]
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'fourludata': fourludata,
               'category': category}
    return render(request, 'index.html', context)


def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda', 'category': category}
    return render(request, 'hakkimizda.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderdiniz")
            return HttpResponseRedirect('/iletisim')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'iletisim.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               'categorydata': categorydata}
    return render(request, 'oteller.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(hotel_id=id)
    comments = Comments.objects.filter(product_id=id, status='True')
    context = {'category': category,
               'product': product,
               'images': images,
               'comments': comments}

    return render(request, 'productdetail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {
                'products': products,
                'category': category,
            }
            return render(request, 'products_search.html', context)
    return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return HttpResponseRedirect('/')
        
        else:
            messages.warning(request,"Lütfen Tekrar Dene")
            return HttpResponseRedirect('/login')
        
    category = Category.objects.all()
    context = {'category': category,
               }

    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password1')
            user = authenticate(username=username , password=password)
            login(request,user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request,"Başarılı")
            return HttpResponseRedirect('/')

    form = SignUpForm()    
    category = Category.objects.all()
    context = {'category': category,
               'form': form,}

    return render(request, 'signup.html', context)
