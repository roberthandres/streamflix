
from django.db import models


class Pelicula(models.Model):

    TIPOS = [
        ('pelicula', 'Película'),
        ('serie', 'Serie'),
    ]

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField()

    imagen_url = models.URLField(blank=True)

    banner_url = models.URLField(blank=True)

    genero = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        default='pelicula'
    )

    fecha_lanzamiento = models.DateField(
        null=True,
        blank=True
    )

    duracion = models.PositiveIntegerField(
        default=0,
        help_text="Duración en minutos"
    )

    calificacion = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0
    )

    destacado = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['-fecha_creacion']
