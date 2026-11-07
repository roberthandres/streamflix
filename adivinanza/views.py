
import random

from django.shortcuts import render
from peliculas.models import Pelicula


def jugar(request):
    peliculas = list(
        Pelicula.objects.filter(tipo='pelicula').exclude(titulo='')
    )

    if not peliculas:
        return render(request, 'adivinanza/jugar.html', {
            'error': 'Todavía no hay películas registradas para jugar.'
        })

    # Seleccionar una película aleatoria
    pelicula = random.choice(peliculas)

    # Guardar la película elegida en la sesión
    request.session['pelicula_id'] = pelicula.id

    contexto = {
        'pista_genero': pelicula.genero,
        'pista_anio': (
            pelicula.fecha_lanzamiento.year
            if pelicula.fecha_lanzamiento else 'Desconocido'
        ),
        'pista_descripcion': pelicula.descripcion[:180] + '...'
        if len(pelicula.descripcion) > 180
        else pelicula.descripcion,
    }

    return render(request, 'adivinanza/jugar.html', contexto)


def comprobar_respuesta(request):
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta', '').strip().lower()
        pelicula_id = request.session.get('pelicula_id')

        if not pelicula_id:
            return jugar(request)

        pelicula = Pelicula.objects.filter(id=pelicula_id).first()

        if pelicula and respuesta == pelicula.titulo.strip().lower():
            resultado = '¡Correcto! Has adivinado la película.'
            acierto = True
        else:
            resultado = 'Respuesta incorrecta. ¡Inténtalo de nuevo!'
            acierto = False

        return render(request, 'adivinanza/resultado.html', {
            'resultado': resultado,
            'acierto': acierto,
            'titulo_correcto': pelicula.titulo if pelicula else '',
        })

    return jugar(request)
