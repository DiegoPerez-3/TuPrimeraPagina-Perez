from django.urls import path

from AppCoder.views import (
    cursos,
    inicio,
    crear_curso,
    editar_curso,
    eliminar_curso,
    ver_curso,
)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("cursos/nuevo/", crear_curso, name="crear_curso"),
    path("cursos/editar/<int:id>/", editar_curso, name="editar_curso"),
    path("cursos/eliminar/<int:id>/", eliminar_curso, name="eliminar_curso"),
    path("cursos/ver/<int:id>/", ver_curso, name="ver_curso"),
]
