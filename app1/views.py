from django.shortcuts import render, get_object_or_404, redirect
from .models import Cancha, Reserva, Complejo
from .forms import CanchaForm, ReservaForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'app1/inicio.html', {})

def cancha(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id)
    canchas = list(Cancha.objects.filter(complejo_id=id_comple))
    return render(request, 'app1/cancha.html', {'canchas': canchas})

@login_required
def cancha_nueva(request):
    if request.method == "POST":
        form = CanchaForm(request.POST)
        if form.is_valid():
            cancha = form.save(commit=False)
            id_comple = Complejo.objects.get(usuario_id=request.user.id)
            cancha.complejo = id_comple
            cancha.fecha_creacion = timezone.now()
            cancha.save()
            return redirect('cancha')
    else:

        form = CanchaForm()
    return render(request, 'app1/cancha_editar.html', {'form': form})

@login_required
def cancha_editar(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    if request.method == "POST":
        form = CanchaForm(request.POST, instance=cancha)
        if form.is_valid():
            cancha = form.save(commit=False)
            cancha.fecha_creacion = timezone.now()
            cancha.save()
            return redirect('cancha')
    else:
        form = CanchaForm(instance=cancha)
    return render(request, 'app1/cancha_editar.html', {'form': form})

def reserva(request):
    reservas = list(Reserva.objects.all())
    return render(request, 'app1/reserva.html', {'reservas': reservas})

@login_required
def reserva_nueva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.fecha_creacion = timezone.now()
            reserva.save()
            return redirect('reserva')
    else:
        id_comple = Complejo.objects.get(usuario_id=request.user.id)
        canchas = list(Cancha.objects.filter(complejo_id=id_comple))
        form = ReservaForm()
    return render(request, 'app1/reserva_editar.html', {'form': form, 'canchas': canchas})

@login_required
def reserva_editar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.fecha_creacion = timezone.now()
            reserva.save()
            return redirect('reserva')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'app1/reserva_editar.html', {'form': form})
