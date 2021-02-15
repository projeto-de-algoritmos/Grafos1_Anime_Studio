from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.home, name='home'),
    path('projeto/', views.projeto, name='projeto'),
]