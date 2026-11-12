
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('juego/', include('adivinanza.urls')),
]
