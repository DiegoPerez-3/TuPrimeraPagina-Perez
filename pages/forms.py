from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["titulo", "subtitulo", "categoria", "contenido", "imagen", "fecha_publicacion"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Análisis de Inception"}),
            "subtitulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Un viaje al subconsciente"}),
            "categoria": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Películas de Acción"}),
            "fecha_publicacion": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
