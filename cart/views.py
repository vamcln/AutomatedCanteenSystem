from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from fooditems.models import Fooditem
from .models import Cart
from django.contrib.auth.decorators import login_required
# Created views for cart
#this is the carts views.py
@login_required(login_url='login')
def cart(request):
    if request.method == "POST":
        id = request.POST['id']
        n = request.POST['nam']
        q = request.POST['quantity']
        c = int(request.POST['costof'])*int(q)
        if Cart.objects.filter(name=n,customer=request.user).exists():
            o = get_object_or_404(Cart, name=n, customer=request.user)
            o.quantity = o.quantity+int(q)
            o.totalcost = o.totalcost+int(c)
            o.save()
        else:
            cart = Cart()
            #k = 0
            cart.name = n
            cart.quantity = q
            cart.totalcost = c
            cart.customer = request.user
            cart.save()
        return redirect('home')
@login_required(login_url='login')
def cart1(request):
    f = Cart.objects.filter(customer=request.user)
    tc = 0
    for i in f:
        tc = tc + i.totalcost
    return render(request,'cart/c.html',{"f":f,'tc':tc})
@login_required(login_url='login')
def cart2(request):
    n = request.POST['nam']
    f = get_object_or_404(Cart, name=n, customer=request.user)
    f.delete()
    return redirect('cart1')
