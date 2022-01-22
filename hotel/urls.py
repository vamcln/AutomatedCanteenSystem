from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bargraph',views.bar,name='bar'),
    path('piechart',views.pie,name='pie'),
    path('linechart',views.line,name='line'),
    path('check',views.check,name='check'),
    path('confirm',views.confirm,name='confirm'),
    path('incentives',views.incentives,name='incentive'),
]
