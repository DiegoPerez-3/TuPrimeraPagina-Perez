from django import forms
from .models import Genero, PeliculaSerie, Resena


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ["nombre", "descripcion"]


class PeliculaSerieForm(forms.ModelForm):
    class Meta:
        model = PeliculaSerie
        fields = ["titulo", "tipo", "genero", "anio", "descripcion"]


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ["pelicula", "autor", "comentario", "puntaje"]


class BusquedaForm(forms.Form):
    texto = forms.CharField(
        max_length=100,
        label="Buscar película o serie",
        required=True
    )