# agenda/forms.py

from django import forms
from .models import Recordatorio
import os

# Ruta absoluta al archivo de palabras prohibidas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROHIBIDAS_PATH = os.path.join(BASE_DIR, 'agenda', 'palabras_prohibidas.txt')

# Cargar palabras prohibidas desde el archivo .txt
def cargar_palabras_prohibidas():
    try:
        with open(PROHIBIDAS_PATH, 'r', encoding='utf-8') as archivo:
            return [line.strip().lower() for line in archivo if line.strip()]
    except FileNotFoundError:
        return []

PALABRAS_PROHIBIDAS = cargar_palabras_prohibidas()

class RecordatorioForm(forms.ModelForm):
    class Meta:
        model = Recordatorio
        fields = ['titulo', 'descripcion', 'fecha', 'hora']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': 'max-width: 200px;'
            }),
            'hora': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'style': 'max-width: 150px;'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = ['%Y-%m-%d']

    def validar_texto(self, campo, valor):
        for palabra in PALABRAS_PROHIBIDAS:
            if palabra in valor.lower():
                raise forms.ValidationError(
                    f"La palabra '{palabra}' no está permitida en el {campo}."
                )

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        self.validar_texto('título', titulo)
        return titulo

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        self.validar_texto('descripción', descripcion)
        return descripcion
