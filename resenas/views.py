from django.shortcuts import render, redirect
from .models import PeliculaSerie, Resena
from .forms import GeneroForm, PeliculaSerieForm, ResenaForm, BusquedaForm


def inicio(request):
    peliculas = PeliculaSerie.objects.all().order_by("-fecha_creacion")[:5]
    resenas = Resena.objects.all().order_by("-fecha")[:5]

    return render(request, "resenas/inicio.html", {
        "peliculas": peliculas,
        "resenas": resenas,
    })


def lista_peliculas(request):
    peliculas = PeliculaSerie.objects.all().order_by("titulo")

    return render(request, "resenas/lista_peliculas.html", {
        "peliculas": peliculas,
    })


def crear_genero(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = GeneroForm()

    return render(request, "resenas/formulario.html", {
        "form": form,
        "titulo": "Crear género",
    })


def crear_pelicula(request):
    if request.method == "POST":
        form = PeliculaSerieForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_peliculas")
    else:
        form = PeliculaSerieForm()

    return render(request, "resenas/formulario.html", {
        "form": form,
        "titulo": "Crear película o serie",
    })


def crear_resena(request):
    if request.method == "POST":
        form = ResenaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ResenaForm()

    return render(request, "resenas/formulario.html", {
        "form": form,
        "titulo": "Crear reseña",
    })


def buscar_pelicula(request):
    form = BusquedaForm(request.GET or None)
    resultados = []
    busqueda_realizada = False

    if form.is_valid():
        texto = form.cleaned_data["texto"]
        resultados = PeliculaSerie.objects.filter(titulo__icontains=texto)
        busqueda_realizada = True

    return render(request, "resenas/buscar.html", {
        "form": form,
        "resultados": resultados,
        "busqueda_realizada": busqueda_realizada,
    })