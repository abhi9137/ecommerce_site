from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from products.models import *

# Create your views here.
def homepage(request,username):
    user=User.objects.get(username=username)
    product1=Products.objects.get(product_id=1111)
    product2=Products.objects.get(product_id=2222)
    product3=Products.objects.get(product_id=3333)
    product4=Products.objects.get(product_id=4444)
    product5=Products.objects.get(product_id=5555)
    product6=Products.objects.get(product_id=6666)
    product_name="a"
    context={
        'username':username,
        'user':user,
        'product1':product1,
        'product2':product2,
        'product3':product3,
        'product4':product4,
        'product5':product5,
        'product6':product6,
    }
    if request.method=="POST":
        return redirect('buy_product',username,product_name)
        
    return render(request,'homepage/homepage.html',context)