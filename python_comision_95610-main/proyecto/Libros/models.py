from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros") 
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=100, blank=True) 
    fecha_pulicacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} -- {self.autor.nombre}"