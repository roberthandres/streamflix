
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jugar, name='jugar'),
    path('comprobar/', views.comprobar_respuesta, name='comprobar_respuesta'),
]
