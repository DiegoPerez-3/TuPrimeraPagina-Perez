from django.contrib import admin

from AppCoder.models import Curso, Estudiante, Profesor, Entregable

# admin.site.register(Curso)
admin.site.register(Estudiante)
# admin.site.register(Profesor)
admin.site.register(Entregable)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'camada', 'modalidad')
    search_fields = ('nombre',)
    list_filter = ('modalidad', 'camada')


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_creacion')
    search_fields = ('apellido',)
    list_filter = ('nombre', 'apellido')
