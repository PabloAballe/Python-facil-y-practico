#importamos las librerias necesarias
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
#definimos donde se reenderizara nuestra vista ademas de la vista que se debe mostrar
    path('', views.index, name="index"),
    #definimos las urls de los posts individualmente
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
