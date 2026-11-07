from django.contrib import admin
from .models import Pelicula


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'genero',
        'tipo',
        'fecha_lanzamiento',
        'calificacion',
        'destacado',
    )

    search_fields = ('titulo', 'genero')

    list_filter = ('tipo', 'genero', 'destacado')