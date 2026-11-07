from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar-api/', views.buscar_series_api, name='buscar_api'),
]