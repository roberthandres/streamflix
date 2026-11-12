

import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Pelicula
from .forms import PeliculaForm


# ==========================================
# PAGINA DE INICIO
# ==========================================

@login_required
@permission_required('peliculas.view_pelicula', raise_exception=True)
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

@login_required
@permission_required('peliculas.view_pelicula', raise_exception=True)
def buscar_series_api(request):

    resultados = []
    error = None
    nombre = request.GET.get('q', '').strip()

    if nombre:
        url = 'https://api.tvmaze.com/search/shows'
        parametros = {'q': nombre}

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


# ==========================================
# EDITAR PELICULA O SERIE
# ==========================================

@login_required
@permission_required('peliculas.change_pelicula', raise_exception=True)
def editar_pelicula(request, id):

    pelicula = get_object_or_404(Pelicula, id=id)

    if request.method == 'POST':
        formulario = PeliculaForm(request.POST, instance=pelicula)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Contenido actualizado correctamente.')
            return redirect('inicio')

    else:
        formulario = PeliculaForm(instance=pelicula)

    contexto = {
        'formulario': formulario,
        'pelicula': pelicula,
    }

    return render(request, 'peliculas/editar.html', contexto)


# ==========================================
# ELIMINAR PELICULA O SERIE
# ==========================================

@login_required
@permission_required('peliculas.delete_pelicula', raise_exception=True)
def eliminar_pelicula(request, id):

    pelicula = get_object_or_404(Pelicula, id=id)

    if request.method == 'POST':
        titulo = pelicula.titulo
        pelicula.delete()

        messages.success(
            request,
            f'"{titulo}" fue eliminado correctamente.'
        )

        return redirect('inicio')

    contexto = {
        'pelicula': pelicula,
    }

    return render(request, 'peliculas/eliminar.html', contexto)
