from django.contrib import admin
from django.urls import path
from .views import home,addtask,deletetask,edittask,updatetask

urlpatterns = [
    path('',home, name='home'),
    path('addtask/', addtask),
    path('deletetask/<int:taskpk>/',deletetask),
    path('edittask/<int:taskpk>/',edittask),
    path('updatetask/<int:taskpk>/update/',updatetask)
]
