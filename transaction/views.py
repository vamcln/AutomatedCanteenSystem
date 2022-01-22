from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from history.models import History
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Transactions
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def money(request):
    p = request.POST['cs']
    if int(p) == 0:
        return redirect('home')
    return render(request,'transaction/pay.html',{'p':p})
@login_required(login_url='login')
def res(request):
    f = Cart.objects.filter(customer=request.user)
    print(f)
    for i in range(0,len(f)):
        h = History()
        h.item = f[i].name
        h.quantity = f[i].quantity
        h.totalcost = f[i].totalcost
        h.customer = f[i].customer
        h.order_date = timezone.datetime.now()
        #h.reserve_time = s
        print(f[i])
        f[i].delete()
        h.save()
        print(h)
    t = Transactions()
    t.customer = request.user
    t.totalcost = (request.POST['cost'])
    t.order_date = timezone.datetime.now()
    t.save()
    #------------------------------------send mail----------------------------------------------
    hi = History.objects.filter(customer=request.user, status="P")
    rec = str(request.user.email)
    html_content = render_to_string('transaction/email.html', {'hi':hi})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives("Your Order", text_content, settings.EMAIL_HOST_USER,[rec])
    email.attach_alternative(html_content,"text/html")
    email.send()
    return redirect('home')
@login_required(login_url='login')
def check(request):
    t = Transactions.objects.filter(customer=request.user)
    return render(request,'transaction/payment.html',{'t':t})
