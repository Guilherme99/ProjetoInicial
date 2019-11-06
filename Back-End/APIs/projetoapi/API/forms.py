from .models import Usuario
from django import forms

class InsereUsuarioForm(forms.ModelForm):
  class Meta:
    # Modelo base
    model = Usuario

    # Campos que estarão no form
    fields = '__all__'

    # Campos que não estarão no form    
    exclude = [
      ''
    ]
