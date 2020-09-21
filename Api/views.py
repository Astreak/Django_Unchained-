from django.shortcuts import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import *
from .serialization import *

def Home(req):
    return HttpResponse("<h1><center> Hello World </center></h1>")

class AuthorApi(viewsets.ModelViewSet):
    queryset=Author.objects.all().order_by("name")
    serializer_class=ApiCreation
