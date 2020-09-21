from django.shortcuts import *
from . import views
from django.views import generic
from .forms import *
from .models import *
import datetime
def home(req):
    return render(req,"New/home.html");

def CreateUser(req):
    if req.method=="POST":
        form=Register(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-home")
    else:
        form=Register()
    return render(req,"New/register.html",{"form":form})

def UpdateTask(req,id):
    number=Todo.objects.get(id=id);
    form=Duty(instance=number)
    if req.method=="POST":
        form=Duty(req.POST,instance=number)
        if form.is_valid():
            form.save()
            return redirect("main-home")
    else:
        form=Duty()
    return render(req,"New/duty.html",{"form":form})
    
def DeleteTask(req,id): 
    number=Todo.objects.get(id=id)
    if req.method=="POST":
        number.delete()
    else:
        return render(req,"New/duty.html");

    
def DutyForm(req):
    if req.method=="POST":
        form=Duty(req.POST)
        if form.is_valid():
            form.save()
            
            return redirect("main-home")
    else:
        form=Duty()
    return render(req,"New/duty.html",{"form":form})

def query(req):
    if req.user.is_authenticated:
        G=req.user.todo_set.all()
        for i in G:
            print(i.text)
        F=datetime.datetime.now()
    else:
        G="NOt";
        F="Authorized";
    GG={
        "T":G,
        "K":F
    }
    
    return render(req,"New/query.html",GG);
