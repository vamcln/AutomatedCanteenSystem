from django.shortcuts import render, redirect
from accounts import *
from .models import Fooditem
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.

@login_required(login_url='login')
def home(request):
    food = Fooditem.objects
    return render(request, 'fooditems/home.html',{'food':food})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home1(request):
    return render(request, 'fooditems/home1.html')
