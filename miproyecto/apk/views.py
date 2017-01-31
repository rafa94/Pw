from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader,context
from .models import Equipo,Jugadores,Partidos
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

def inicio(request):
	return render(request,'index.html')


def ver_equipo(request):
	equipo = Equipo.objects.all()
	context = {'equipos': equipo}
	return render(request,'equipos.html',context)

def	ver_clasificacion(request):
	clasificacion = Equipo.objects.order_by('pos')
	context = {'clasificaciones': clasificacion}
	return render(request,'clasificacion.html',context)


def ver_jornada(request):
	jornada = Partidos.objects.order_by('dia')
	context = {'jornadas' : jornada }
	return render(request,'partidos.html',context)

def ver_jugadores_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    jugadores = equipo.plantilla.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})

