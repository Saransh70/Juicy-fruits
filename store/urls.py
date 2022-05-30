from django.contrib import admin
from django.urls import path
from .views import index , signup , login
from store import views
urlpatterns = [
    path('', index , name='homepage'),
    path('signup' , views.signup, name='signup'),
    path('login' , views.login , name='login')
]
