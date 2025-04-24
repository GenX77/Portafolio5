# agenda/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Recordatorio
from .forms import RecordatorioForm
from datetime import datetime, timedelta
from django.utils.timezone import make_aware, now

def inicio(request):
    ahora = make_aware(datetime.now())
    hoy = ahora.date()
    en_12_horas = ahora + timedelta(hours=12)

    vencidas = Recordatorio.objects.filter(
        fecha__lt=hoy,
        hecho=False
    ) | Recordatorio.objects.filter(
        fecha=hoy,
        hora__lt=ahora.time(),
        hecho=False
    )

    proximos = Recordatorio.objects.filter(
        fecha=hoy,
        hora__gte=ahora.time(),
        hora__lte=(ahora + timedelta(hours=4)).time(),
        hecho=False
    )

    hoy_recordatorios = Recordatorio.objects.filter(fecha=hoy, hecho=False)

    tareas_proximas_12h = Recordatorio.objects.filter(
        hecho=False,
        fecha__gte=hoy,
        fecha__lte=en_12_horas.date()
    ).order_by('fecha', 'hora')

    return render(request, 'agenda/inicio.html', {
        'hay_hoy': hoy_recordatorios.exists(),
        'proximos': proximos.exists(),
        'hay_vencidos': vencidas.exists(),
        'tareas_12h': tareas_proximas_12h,
    })

def agregar_recordatorio(request):
    if request.method == 'POST':
        form = RecordatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:listar_recordatorios')
    else:
        form = RecordatorioForm()
    return render(request, 'agenda/agregar_recordatorio.html', {'form': form})

def listar_recordatorios(request):
    recordatorios = Recordatorio.objects.all().order_by('fecha', 'hora')
    return render(request, 'agenda/listar_recordatorios.html', {'recordatorios': recordatorios})

def editar_recordatorio(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    if request.method == 'POST':
        form = RecordatorioForm(request.POST, instance=recordatorio)
        if form.is_valid():
            form.save()
            return redirect('agenda:listar_recordatorios')
    else:
        form = RecordatorioForm(instance=recordatorio)
    return render(request, 'agenda/editar_recordatorio.html', {'form': form})

def toggle_hecho(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)
    recordatorio.hecho = not recordatorio.hecho
    recordatorio.save()
    return redirect('agenda:listar_recordatorios')

def recordatorios_hoy(request):
    hoy = now().date()
    recordatorios = Recordatorio.objects.filter(fecha=hoy, hecho=False).order_by('hora')
    return render(request, 'agenda/listar_recordatorios.html', {'recordatorios': recordatorios})

def recordatorios_proximos(request):
    hoy = now().date()
    ahora = now()
    recordatorios = Recordatorio.objects.filter(
        fecha=hoy,
        hora__gte=ahora.time(),
        hora__lte=(ahora + timedelta(hours=4)).time(),
        hecho=False
    ).order_by('fecha', 'hora')
    return render(request, 'agenda/listar_recordatorios.html', {'recordatorios': recordatorios})

def recordatorios_sin_realizar(request):
    recordatorios = Recordatorio.objects.filter(hecho=False).order_by('fecha', 'hora')
    return render(request, 'agenda/listar_recordatorios.html', {'recordatorios': recordatorios})

def recordatorios_vencidos(request):
    ahora = make_aware(datetime.now())
    hoy = ahora.date()
    recordatorios = Recordatorio.objects.filter(
        fecha__lt=hoy,
        hecho=False
    ) | Recordatorio.objects.filter(
        fecha=hoy,
        hora__lt=ahora.time(),
        hecho=False
    )
    recordatorios = recordatorios.order_by('fecha', 'hora')
    return render(request, 'agenda/listar_recordatorios.html', {'recordatorios': recordatorios})

def recordar_dia(request):
    fecha_seleccionada = request.GET.get('fecha')
    recordatorios = []
    ayer = (now() - timedelta(days=1)).date()

    if fecha_seleccionada:
        try:
            fecha = datetime.strptime(fecha_seleccionada, "%Y-%m-%d").date()
            if fecha <= ayer:
                recordatorios = Recordatorio.objects.filter(fecha=fecha).order_by('hora')
        except ValueError:
            fecha = None
    else:
        fecha = None

    return render(request, 'agenda/recordar_dia.html', {
        'recordatorios': recordatorios,
        'fecha_seleccionada': fecha_seleccionada,
        'ayer': ayer.isoformat()
    })
