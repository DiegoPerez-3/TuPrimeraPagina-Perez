from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class PeliculaSerie(models.Model):
    TIPO_CHOICES = [
        ("Pelicula", "Película"),
        ("Serie", "Serie"),
    ]

    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    anio = models.PositiveIntegerField()
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"


class Resena(models.Model):
    PUNTAJE_CHOICES = [(i, i) for i in range(1, 11)]

    pelicula = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    puntaje = models.IntegerField(choices=PUNTAJE_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.autor} para {self.pelicula.titulo}"