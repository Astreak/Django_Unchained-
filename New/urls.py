from django.urls import path,include
from django.contrib.auth.models import User
from django.views import generic
from .models import *
from .forms import *
from . import views

urlpatterns=[
    path('',views.home,name="main-home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/',views.CreateUser,name="main-register"),
    path('duty/',views.DutyForm,name="main-duties"),
    path('tasks/',views.query,name="main-task"),
    path('update_task/<int:id>',views.UpdateTask,name="update_task"),
    path('delete_task/<int:id>',views.DeleteTask,name="delete_task"),
    
    
    
    
    
]

