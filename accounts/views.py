from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.cache import cache_control
# Create your views here.
def signup(request):
    if request.method == "POST":
        p = request.POST['pass1']
        if len(p) < 6:
            return render(request, 'accounts/signup.html', {'er':'Password length should be greater than 6'})
        if '@gmail.com' not in str(request.POST['email']):
            return render(request, 'accounts/signup.html', {'er':'Invalid email id'})
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'er':'Username already taken'})
                print(len(p))
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],email=request.POST['email'], password=request.POST['pass1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'er':'Passwords does not match'})
    else:
        return render(request, 'accounts/signup.html')
#----------------------------------------------------------------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],password=request.POST['pass1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'er':'Username and password does not match'})
    else:
        return render(request, 'accounts/login.html')
    # TODO: make correct render
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home1')
    return render(request, 'accounts/signup.html')
def profile(request):
    u = request.user
    return render(request, 'accounts/profile.html',{'u':u})
