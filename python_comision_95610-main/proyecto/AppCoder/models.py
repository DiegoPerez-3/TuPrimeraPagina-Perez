from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# DB --> Tabla Curso
class Curso(models.Model):
    class Modalidad(models.TextChoices):
        ONLINE = 'ONL', 'Online'
        PRESENCIAL = 'PRE', 'Presencial'
        HIBRIDO = 'HIB', 'Hibrido'

    nombre = models.CharField(max_length=20)
    camada = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(1000000)
    ])
    modalidad = models.CharField(
        max_length=3,
        choices=Modalidad.choices,
        default=Modalidad.PRESENCIAL
    )
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} -- {self.camada}"


# DB -- Tabla Entregable (Columnas: nombre - fecha - entregado)
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"estudiante: {self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    profesion = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"profesor: {self.apellido}, {self.nombre}"
