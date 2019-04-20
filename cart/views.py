
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from .models import Product,Quant,Discount,Det,Order
#from .forms import Prod
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy# Create your views here.
from .filters import UserFilter

count=0

def search(request):
    item=[]
    if request.method=='POST':
        val=request.POST.get('example-search-input')
        item=Product.objects.filter(product_name=val)
        if item:
             return render(request,'cart/user_list.html',{'item':item})
        else:
             return redirect('cart/detail/')

    return render(request,'cart/user_list.html')

def detail(request,product_id):
    quant=[]
    prod=Product.objects.get(id=product_id)
    quant=Quant.objects.filter(product=prod)
    if request.method =='POST':
        val=request.POST.get('exampleFormControlSelect1')
        price=request.POST.get('price')
        discount=request.POST.get('disc')
        quantity=request.POST.get('quants')
       # print(discount)
        if discount=="% Discount":
            disc=request.POST.get('disc_val')
            a=int(price)
            b=int(disc)
            a=a-((a*b)/100)
        elif discount=="Flat Discount":
            disc = request.POST.get('disc_val')
            a = int(price)
            b = int(disc)
            a=a-b
        elif discount=="Final Price":
            disc = request.POST.get('disc_val')
            a = int(price)
            b = int(disc)
            a=b
        q = int(quantity)
        x= int(val)
        for size in quant:
            l = int(size.quantity)
            m=int(size.size_val)
            if x is m:
                l = l - q
                print(l)
                size.quantity=l
                size.save()

        net_amount=q*a
        form = Order.objects.create(prod=prod,price=a,size=val,quantity=quantity,disc=discount,discount_offered=b,net_amount=net_amount)
        form.save()

        #return HttpResponse('<h1>HI</h1>')
        return redirect('/search/cart/')


    else:
        dict={}
        v=Product.objects.filter(id=product_id).values()
        val=Product.objects.get(id=product_id)
        size=Quant.objects.filter(product=val)
        for x in size:
            dict[x.size_val]=x.quantity

        return render(request,'cart/detail.html',{'dict':dict,'val':val,'v':v})
    return render(request, 'cart/deatil.html')

def cart(request):
    order=Order.objects.all()
    return render(request,'cart/index.html',{'order':order})

def det(request,order_id):
    val=Order.objects.get(id=order_id)


    if request.method=='POST':
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        contact=request.POST.get('contact')
        addr=request.POST.get('addr')
        pay=request.POST.get('gridRadios')
        deli=request.POST.get('delivery')


        print(timezone.now())

        form=Det.objects.create(item=val,name=name,add=addr,contact=contact,email=mail,mode=pay,deliver=deli)
        form.save()
        subject = 'Thank You for choosing us'
        message = 'Welcome'
        from_email = settings.EMAIL_HOST_USER
        to_list = [mail, 'settings.EMAIL_HOST_USER']
        send_mail(subject=subject, from_email=from_email, recipient_list=to_list, message=message, fail_silently=True)

        return redirect('search/cart/form/')
    return render(request,'cart/add.html')

def delete(request,order_id):
    Order.objects.filter(id=order_id).delete()
    return redirect('/search/cart/')

def form(request):
    return HttpResponse('<h1>Hello</h1>')

