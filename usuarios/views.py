
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views.decorators.http import require_POST


# REGISTRO
def registro(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()

            grupo, creado = Group.objects.get_or_create(
                name='Usuario'
            )

            usuario.groups.add(grupo)

            # Limpiar mensajes anteriores
            list(messages.get_messages(request))

            messages.success(
                request,
                'Tu cuenta fue creada correctamente.'
            )

            return redirect('login')

    else:
        formulario = UserCreationForm()

    return render(
        request,
        'usuarios/registro.html',
        {'formulario': formulario}
    )


# INICIAR SESION
def iniciar_sesion(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        formulario = AuthenticationForm(
            request,
            data=request.POST
        )

        if formulario.is_valid():

            usuario = formulario.get_user()

            # Limpiar mensajes anteriores
            list(messages.get_messages(request))

            login(request, usuario)

            messages.success(
                request,
                f'Bienvenido, {usuario.username}.'
            )

            return redirect('inicio')

    else:
        formulario = AuthenticationForm()

    return render(
        request,
        'usuarios/login.html',
        {'formulario': formulario}
    )


# CERRAR SESION
@require_POST
def cerrar_sesion(request):

    # Eliminar mensajes anteriores
    list(messages.get_messages(request))

    # Cerrar sesión
    logout(request)

    # Mostrar únicamente este mensaje
    messages.success(
        request,
        'Has cerrado sesión correctamente.'
    )

    return redirect('inicio')
