from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250)
    categoria = models.CharField(max_length=100, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="pages/", blank=True, null=True)
    fecha_publicacion = models.DateField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pages")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_publicacion", "-creado"]
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("page_detail", kwargs={"pk": self.pk})
