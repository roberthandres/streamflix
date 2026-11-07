import requests

from django.shortcuts import render
from .models import Pelicula


# ==========================================
# PAGINA DE INICIO
# ==========================================

def inicio(request):

    destacada = Pelicula.objects.filter(destacado=True).first()

    peliculas = Pelicula.objects.filter(tipo='pelicula')

    series = Pelicula.objects.filter(tipo='serie')

    contexto = {
        'destacada': destacada,
        'peliculas': peliculas,
        'series': series,
    }

    return render(request, 'inicio.html', contexto)


# ==========================================
# BUSCAR SERIES EN TVMAZE
# ==========================================

def buscar_series_api(request):

    resultados = []
    error = None

    nombre = request.GET.get('q', '').strip()

    if nombre:

        url = 'https://api.tvmaze.com/search/shows'

        parametros = {
            'q': nombre
        }

        try:

            respuesta = requests.get(
                url,
                params=parametros,
                timeout=15
            )

            respuesta.raise_for_status()

            datos = respuesta.json()

            resultados = [
                item.get('show', {})
                for item in datos
            ]

        except requests.exceptions.RequestException as e:

            print("ERROR TVMAZE:", str(e))

            error = 'No fue posible consultar la API de series.'

    contexto = {
        'resultados': resultados,
        'nombre': nombre,
        'error': error,
    }

    return render(request, 'buscar_api.html', contexto)