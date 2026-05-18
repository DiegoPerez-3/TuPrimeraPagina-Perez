from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]
        widgets = {
            "recipient": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Asunto"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Escribe tu mensaje aquí..."}),
        }
