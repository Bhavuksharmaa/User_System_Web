from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('createuser',views.createusers,name="createuser"),
    path("about",views.about,name='about'),
    path("service",views.service,name='service'),
    path("contact",views.contact,name='contact')
]