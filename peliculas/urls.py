
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar-api/', views.buscar_series_api, name='buscar_api'),

    path(
        'editar/<int:id>/',
        views.editar_pelicula,
        name='editar_pelicula'
    ),

    path(
        'eliminar/<int:id>/',
        views.eliminar_pelicula,
        name='eliminar_pelicula'
    ),
]
