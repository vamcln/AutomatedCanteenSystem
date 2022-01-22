from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('cart', views.money, name='payment'),
    path('home', views.res, name='pay2'),
    path('payments', views.check, name='pay3'),
]
