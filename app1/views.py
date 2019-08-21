from django.shortcuts import render, get_object_or_404, redirect
from .models import Cancha, Reserva, Complejo, Suscripcion
from .forms import ComplejoForm, CanchaForm, ReservaForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
import pytz
import datetime
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

#Inicio para realizar login e inicio logueado
def inicio(request):
    usuario = ''
    complejo = ''
    comentarios = ''
    autores = ''
    if(request.user.is_authenticated):
        usuario = request.user
        if (usuario.is_staff == 0) or (usuario.is_superuser == 1):
            return redirect('accounts/logout/')
        complejo = Complejo.objects.get(usuario_id=request.user.id)
        comentarios = list(Suscripcion.objects.filter(complejo_id=complejo))
    return render(request, 'app1/inicio.html', {'usuario': usuario, 'complejo': complejo, 'comentarios': comentarios, 'autores': autores})

#Formulario para actualizar la información del Complejo
@login_required
def complejo_update(request):
    complejo = Complejo.objects.get(usuario_id=request.user.id)
    if request.method == "POST":
        form = ComplejoForm(request.POST, request.FILES, instance=complejo)
        if form.is_valid():
            complejo = form.save(commit=False)
            complejo.save()
            return redirect('inicio')
    else:
        form = ComplejoForm(instance=complejo)
    return render(request, 'app1/complejo_editar.html', {'titulo': 'Editar información del Complejo', 'form': form})

#Listado de canchas del complejo
@login_required
def cancha(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id)
    canchas = list(Cancha.objects.filter(complejo_id=id_comple))
    return render(request, 'app1/cancha.html', {'titulo': 'Listado de canchas', 'canchas': canchas})

#Formulario para ingresar una nueva cancha al complejo
@login_required
def cancha_nueva(request):
    if request.method == "POST":
        form = CanchaForm(request.POST, request.FILES)
        if form.is_valid():
            cancha = form.save(commit=False)
            id_comple = Complejo.objects.get(usuario_id=request.user.id)
            cancha.complejo = id_comple
            cancha.fecha_creacion = timezone.now()
            cancha.save()
            messages.success(request, '¡ Cancha guardada con éxito !')
            return redirect('cancha')
    else:
        form = CanchaForm()
    return render(request, 'app1/cancha_editar.html', {'titulo': 'Agregar cancha', 'form': form})

#Formulario para editar la información de una cancha existente
@login_required
def cancha_editar(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    if request.method == "POST":
        form = CanchaForm(request.POST, request.FILES, instance=cancha)
        if form.is_valid():
            cancha = form.save(commit=False)
            cancha.fecha_creacion = timezone.now()
            #cancha.foto_cancha = request.FILES.get('foto_cancha')
            cancha.save()
            messages.success(request, '¡ Cancha modificada con éxito !')
            return redirect('cancha')
    else:
        id_comple = Complejo.objects.get(usuario_id=request.user.id)
        canchas = list(Cancha.objects.filter(complejo_id=id_comple))
        cancha_encontrada = False
        for cancha_act in canchas:
            if cancha == cancha_act:
                cancha_encontrada = True
        if cancha_encontrada == False:
            messages.error(request, '¡ No tiene acceso a ese enlace !')
            return redirect('cancha')
        form = CanchaForm(instance=cancha)
    return render(request, 'app1/cancha_editar.html', {'titulo': 'Editar cancha', 'form': form})

#Listado de reservas activas del Compplejo
@login_required
def reserva(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id)
    canchas = list(Cancha.objects.filter(complejo_id=id_comple))
    reservas = Reserva.objects.filter(cancha_id__in=canchas, estado_reserva=1).order_by('fecha_reserva', 'hora_inicio')

    #Actualización del estado de reservas (Cancelación de reservas vencidas)
    ecuador = pytz.timezone('America/Guayaquil')
    fecha_hoy = datetime.datetime.now(ecuador)
    hora_actual = fecha_hoy.strftime("%H:%M")
    hora_actual = datetime.datetime.strptime(hora_actual, "%H:%M").time()
    fecha_hoy = fecha_hoy.strftime("%Y-%m-%d")
    fecha_hoy = datetime.datetime.strptime(fecha_hoy, "%Y-%m-%d").date()

    actualizacionReservas = []
    for reserva_act in reservas:
        if(reserva_act.fecha_reserva == fecha_hoy and reserva_act.hora_fin < hora_actual):
            Reserva.objects.filter(id=reserva_act.id).update(estado_reserva=0)
        else:
            actualizacionReservas.append(reserva_act)
    return render(request, 'app1/reserva.html', {'titulo': 'Listado de reservas activas','reservas': actualizacionReservas})

#Formulario para agregar una nueva reserva
@login_required
def reserva_nueva(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id) #Obtener el complejo que le pertenece al administador logueado
    canchas = list(Cancha.objects.filter(complejo_id=id_comple)) #Obtener las canchas que le pertenecen a ese complejo
    reservas = Reserva.objects.filter(cancha_id__in=canchas, estado_reserva=1)

    if request.method == "POST": #Si se envia datos del formulario:
    	form = ReservaForm(request.POST)
    	if form.is_valid(): #Si el formulario es válido:
            reserva = form.save(commit=False) #Los datos enviados no se guardan aún
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
                messages.success(request, '¡ Reserva guardada con éxito !')
                return redirect('reserva')
            else:
                messages.error(request, 'Este cancha no pertenece al complejo')
                return redirect('reserva')
    else:
        id_comple = Complejo.objects.get(usuario_id=request.user.id)
        canchas = list(Cancha.objects.filter(complejo_id=id_comple, estado_cancha=1))
        usuarios_suscritos = Suscripcion.objects.filter(complejo_id=id_comple, suscripcion=1)
        suscritos = []
        for usuario_suscrito in usuarios_suscritos:
            suscritos.append(usuario_suscrito.usuario_id)
        Usuario_final = User.objects.get(username='Usuario_final')
        suscritos.append(Usuario_final.id)
        usuarios = User.objects.filter(is_staff=0, id__in=suscritos)
        form = ReservaForm()
    return render(request, 'app1/reserva_editar.html', {'titulo': 'Agregar reserva', 'form': form, 'canchas': canchas, 'usuarios': usuarios, 'complejo': id_comple})

#Formulario para cancelar la reserva
@login_required
def reserva_editar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        Reserva.objects.filter(id=pk).delete()
        messages.success(request, '¡ Reserva cancelada !')
        return redirect('reserva')
    else:
        id_comple = Complejo.objects.get(usuario_id=request.user.id)
        canchas = list(Cancha.objects.filter(complejo_id=id_comple))
        reserva_encontrada = False
        for cancha in canchas:
            if reserva.cancha == cancha:
                reserva_encontrada = True
        if reserva_encontrada == False or reserva.estado_reserva == False:
            messages.error(request, '¡ No tiene acceso a ese enlace !')
            return redirect('reserva')
    return render(request, 'app1/reserva_modificar.html', {'titulo': 'Cancelar reserva', 'reserva': reserva})

#Reporte de todas las reservas realizadas (activas e inactivas)
@login_required
def reporte_reservas(request):
    id_comple = Complejo.objects.get(usuario_id=request.user.id)
    canchas = list(Cancha.objects.filter(complejo_id=id_comple))
    reservas = Reserva.objects.filter(cancha_id__in=canchas).order_by('fecha_reserva', 'hora_inicio')

    consulta_mes = request.GET.get("buscar_mes")
    consulta_desde = request.GET.get("buscar_desde")
    consulta_hasta = request.GET.get("buscar_hasta")
    if consulta_mes:
        reservas = Reserva.objects.filter(Q(fecha_reserva__icontains = consulta_mes), cancha_id__in=canchas).order_by('fecha_reserva', 'hora_inicio')
    elif consulta_desde or consulta_hasta:
        if (consulta_desde == "") or (consulta_hasta == ""):
            messages.error(request, 'Si desea buscar por rango de fechas debe llenar ambos campos (desde - hasta)')
            return redirect('reporte_reservas')
        else:
            reservas = Reserva.objects.filter(Q(fecha_reserva__range=[consulta_desde, consulta_hasta]), cancha_id__in=canchas).order_by('fecha_reserva', 'hora_inicio')
    nro_reservas = reservas.count()
    total_ingresos = 0
    for reserva in reservas:
        total_ingresos = total_ingresos + reserva.valor_total

    paginator = Paginator(reservas, 8)
    page = request.GET.get('page')
    reservas = paginator.get_page(page)

    parametros = request.GET.copy()
    if parametros.get('page') != None:
        del parametros['page']

    return render(request, 'app1/reporte_reservas.html', {'reservas': reservas, 'parametros': parametros, 'nro_reservas': nro_reservas, 'total_ingresos': total_ingresos})
