from django import forms

from AppCoder.models import Curso

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    modalidad = forms.ChoiceField(choices=[
        ('ONL', 'Online'),
        ('PRE', 'Presencial'),
        ('HIB', 'Hibrido')
    ]
    )

class CursoModelForm(forms.ModelForm):
    # campo_prueba = forms.CharField(max_length=20)

    class Meta:
        model = Curso
        fields = [ "nombre", "camada", "modalidad"]
        

