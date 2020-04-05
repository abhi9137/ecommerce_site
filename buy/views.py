from django.shortcuts import render,redirect
from .forms import *
from products.models import *
from buy.models import *
# Create your views here.
def buy_products(request,username,product_name):
    
    print("in buy")
    print(product_name)
    product_obj=Products.objects.get(product_name=product_name)
    product_id=product_obj.product_id
    obj=Buy.objects.create(cust_name=username,product_id=product_id)
    product1=Products.objects.get(product_id=1111)
    product2=Products.objects.get(product_id=2222)
    product3=Products.objects.get(product_id=3333)
    product4=Products.objects.get(product_id=4444)
    product5=Products.objects.get(product_id=5555)
    product6=Products.objects.get(product_id=6666)

    context={
        'username':username,
        'product1':product1,
        'product2':product2,
        'product3':product3,
        'product4':product4,
        'product5':product5,
        'product6':product6,
    }
    return redirect('homepage_log',username)

def cart(request,username):
    print("in")
    buy_objects=Buy.objects.filter(cust_name=username)
    print(buy_objects)
    l1=[]
    total=0
    for i in buy_objects:
        print(i.product_id)
        l1.append(Products.objects.get(product_id=i.product_id))
    for i in l1:
        total=total+i.product_price
    print(l1)
    context={
        'total':total,
        'list':l1,
        'username':username
    }
    # product_objects=Products.objects.get()
    return render(request,'buy/cart.html',context)
