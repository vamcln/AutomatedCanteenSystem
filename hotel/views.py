from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from history.models import History
from datetime import date
import calendar
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def bar(request):
    labels = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    data = []
    count = {}
    for l in labels:
        count[l] = 0
    queryset = History.objects.all()
    today = date.today()
    m = today.strftime("%m")
    for h in queryset:
        x = h.order_date
        mon = x.strftime("%m")
        if(mon != m):
            break
        day = str(x.strftime("%A"))
        if day not in labels:
            labels.append(day)
        if day not in count:
            count[day] = 0
        var = count[day]
        count[day] = var + 1
    for l in labels:
        data.append(count[l])


    return render(request,'hotel/bar.html',{
        'labels': labels,
        'data': data,
    })
def pie(request):
    labels = []
    data = []
    count = {}
    today = date.today()
    m = today.strftime("%m")
    queryset = History.objects.all()
    for h in queryset:
        it = h.item
        qty = h.quantity
        dte = h.order_date
        mn = dte.strftime("%m")
        if(mn != m):
            break
        if it not in labels:
            labels.append(it)
        if it not in count:
            count[it] = 0
        var = count[it]
        count[it] = var + qty
    for l in labels:
        data.append(count[l])


    labes = labels[:5]
    dat = data[:5]
    return render(request, 'hotel/pie.html', {
        'labels': labes,
        'data': dat,
    })
def line(request):
    labels = []
    data = []
    for i in range(1,29):
        labels.append(str(i))

    today = date.today()
    m = today.strftime("%m")
    std = [1,3,5,7,8,10,12]
    revenue = {}
    if(m!=2):
        labels.append('29')
        labels.append('30')
    if m in std:
        labels.append('31')
    for l in labels:
        revenue[l] = 0

    queryset = History.objects.order_by('-order_date')
    for h in queryset:
        dte = h.order_date
        cst = h.totalcost
        year = dte.year
        mnth = dte.strftime("%m")
        dtnum = dte.strftime("%d")
        if(mnth != m):
            break
        if dtnum not in revenue:
            revenue[dtnum] = 0
        var = revenue[dtnum]
        revenue[dtnum] = var + cst


    for l in labels:
        data.append(revenue[l])
    return render(request, 'hotel/line.html', {
        'labels': labels,
        'data': data
    })
def base(request):
    return render(request,'hotel/main.html')
def check(request):
    nam = request.POST['username']
    user = User.objects.get(username=nam)
    h = History.objects.filter(customer=user,status="P")
    return render(request,'hotel/show.html',{'h':h,'nam':nam})
def confirm(request):
    nam = request.POST['nam']
    print(nam)
    user = User.objects.get(username=nam)
    h = History.objects.filter(customer=user)
    for j in h:
        j.status="C"
        j.save()
    return redirect('base')

def incentives(request):
    res = []
    count = {}
    today = date.today()
    m = today.strftime("%m")
    queryset = History.objects.order_by('-order_date')
    for h in queryset:
        us = h.customer
        price = h.totalcost
        dt = h.order_date
        dtm = dt.strftime("%m")
        if(dtm != m):
            break
        if us not in res:
            res.append(us)
        if us not in count:
            count[us] = 0
        var = count[us]
        count[us] = var + price

    r = dict(sorted(count.items(),key=lambda item: item[1],reverse = True))
    nm = list(r.keys())
    nm = nm[:5]
    cp = list(r.values())
    cp = cp[:5]
    return render(request, 'hotel/incentives.html',{'names':nm,'costspent':cp})
