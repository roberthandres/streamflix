
from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula

        fields = [
            'titulo',
            'descripcion',
            'imagen_url',
            'banner_url',
            'genero',
            'tipo',
            'fecha_lanzamiento',
            'duracion',
            'calificacion',
            'destacado',
        ]

        widgets = {
            'fecha_lanzamiento': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'descripcion': forms.Textarea(
                attrs={'rows': 4}
            ),
        }
