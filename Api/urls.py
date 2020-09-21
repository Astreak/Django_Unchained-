from django.urls import path,include
from . import views
from rest_framework import routers
Router=routers.DefaultRouter()
Router.register(r"Author",views.AuthorApi)
urlpatterns=[
    path("home/",views.Home,name="main-api"),
    path('',include(Router.urls)),
    path('api-auth/',include("rest_framework.urls",namespace="rest_frameworks")),
    
]