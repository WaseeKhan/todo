from django.contrib import admin
from django.urls import path
from .views import home,addform

urlpatterns = [
    path('',home, name='home'),
    path('addform/',addform, name='addform'),
]
