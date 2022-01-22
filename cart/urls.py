from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('cart1', views.cart1, name='cart1'),
    path('delete', views.cart2, name='cart2'),
]
