
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
]


