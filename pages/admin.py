from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "fecha_publicacion", "creado")
    list_filter = ("categoria", "fecha_publicacion", "autor")
    search_fields = ("titulo", "subtitulo", "contenido")
