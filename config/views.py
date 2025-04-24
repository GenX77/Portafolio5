# config/views.py — vista básica para la raíz

from django.shortcuts import render

def hola_mundo(request):
    return render(request, 'index.html')
