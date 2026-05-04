from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("peliculas/", views.lista_peliculas, name="lista_peliculas"),
    path("crear-genero/", views.crear_genero, name="crear_genero"),
    path("crear-pelicula/", views.crear_pelicula, name="crear_pelicula"),
    path("crear-resena/", views.crear_resena, name="crear_resena"),
    path("buscar/", views.buscar_pelicula, name="buscar_pelicula"),
    path("editar-pelicula/<int:id>/", views.editar_pelicula, name="editar_pelicula"),
    path("eliminar-pelicula/<int:id>/", views.eliminar_pelicula, name="eliminar_pelicula"),
]