from django.shortcuts import render, get_object_or_404, redirect
from .models import Cancha, Reserva, Complejo
from .forms import CanchaForm, ReservaForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
import pytz
import datetime
# Create your views here.
def inicio(request):
	usuario = request.user
	return render(request, 'app1/inicio.html', {'usuario': usuario})

@login_required
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

@login_required
def reserva(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id)
    canchas = list(Cancha.objects.filter(complejo_id=id_comple))
    reservs = list(Reserva.objects.all())
    reservas = []
    for reserva in reservs:
    	for cancha in canchas:
    		if reserva.cancha_id == cancha.id:
    			reservas.append(reserva)
    return render(request, 'app1/reserva.html', {'reservas': reservas})

@login_required
def reserva_nueva(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id) #Obtener el complejo que le pertenece al administador logueado
    canchas = list(Cancha.objects.filter(complejo_id=id_comple)) #Obtener las canchas que le pertenecen a ese complejo
    reservs = list(Reserva.objects.all()) #Obtener todas las reservas 
    reservas = [] #Arreglo para guardar todas las reservas del complejo
    for reserva1 in reservs: #Recorrer todas las reservas 
        for cancha in canchas: #Recorrer todas las canchas del complejo
            if reserva1.cancha_id == cancha.id:
            	reservas.append(reserva1) #Si la cancha reservada es igual a una cancha del complejo se agrega la reserva al arreglo 
    if request.method == "POST": #Si se envia datos del formulario:
    	form = ReservaForm(request.POST)
    	if form.is_valid(): #Si el formulario es válido:
            reserva = form.save(commit=False) #Los datos enviados no se guardan aún
			# if para definir el horario de entrada y salida: 08:00 a 23:00
            #Control para el input de usuario: 
            user_ing = User.objects.get(id=reserva.usuario.id) #Se obtiene el usuario ingresado 
            if user_ing.is_staff == 1: #Si el usuario ingresado es staff:
                messages.error(request, 'El usuario ingresado no puede realizar reservas')
                return redirect('reserva')
            #Control para el input de fecha:
            ecuador = pytz.timezone('America/Guayaquil')
            fecha_ac = datetime.datetime.now(ecuador)
            fecha_ac = fecha_ac.strftime("%Y-%m-%d")
            fecha_ac = datetime.datetime.strptime(fecha_ac, "%Y-%m-%d").date()
            fecha_sup = datetime.datetime.strptime("2019-12-31", "%Y-%m-%d").date()
            if (reserva.fecha_reserva < fecha_ac) or (reserva.fecha_reserva > fecha_sup):
                messages.error(request, 'La fecha ingresada no es válida')
                return redirect('reserva')
            #Control para el input de horas (hora_inicio y hora_fin):
            if reserva.hora_inicio > reserva.hora_fin:
                messages.error(request, 'La hora ingresada no es válida')
                return redirect('reserva')
            mint_hi = reserva.hora_inicio.strftime("%H:%M")
            mint_hi = mint_hi[3:]
            mint_hi = int(mint_hi)
            mint_hf = reserva.hora_fin.strftime("%H:%M")
            mint_hf = mint_hf[3:]
            mint_hf = int(mint_hf)
            if (mint_hi != 0 and mint_hi != 30) or (mint_hf != 0 and mint_hf != 30):
                messages.error(request, 'La hora ingresada no es válida')
                return redirect('reserva')
            compr = 0
            for cancha in canchas:
                if reserva.cancha_id == cancha.id:
                    compr = 1
            if compr == 1:
                for reserv in reservas:
                    if reserv.cancha_id == reserva.cancha_id and reserv.fecha_reserva == reserva.fecha_reserva and reserv.hora_inicio == reserva.hora_inicio and reserv.hora_fin == reserva.hora_fin:
                        messages.error(request, 'La cancha está ocupada')
                        return redirect('reserva')
                    elif reserv.cancha_id == reserva.cancha_id and reserv.fecha_reserva == reserva.fecha_reserva and ((reserva.hora_inicio > reserv.hora_inicio and reserva.hora_inicio < reserv.hora_fin) or (reserva.hora_fin > reserv.hora_inicio and reserva.hora_fin < reserv.hora_fin) or (reserva.hora_inicio == reserv.hora_inicio or reserva.hora_fin == reserv.hora_fin) or (reserva.hora_inicio < reserv.hora_inicio and reserva.hora_fin > reserv.hora_fin)):
                        messages.error(request, 'La cancha está ocupada')
                        return redirect('reserva')
                reserva.fecha_creacion = timezone.now()
                reserva.save()
                messages.success(request, 'Reserva guardada con éxito')
                return redirect('reserva')
            else:
                messages.error(request, 'Este cancha no pertenece al complejo')
                return redirect('reserva')
    else:
        id_comple = Complejo.objects.get(usuario_id=request.user.id)
        canchas = list(Cancha.objects.filter(complejo_id=id_comple))
        usuarios = list(User.objects.filter(is_staff=0))
        form = ReservaForm()
    return render(request, 'app1/reserva_editar.html', {'form': form, 'canchas': canchas, 'usuarios': usuarios})

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
        id_comple = Complejo.objects.get(usuario_id=request.user.id)
        canchas = list(Cancha.objects.filter(complejo_id=id_comple))
        usuarios = list(User.objects.filter(is_staff=0))
        form = ReservaForm(instance=reserva)
    return render(request, 'app1/reserva_editar.html', {'form': form, 'canchas': canchas, 'usuarios': usuarios})
