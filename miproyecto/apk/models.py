from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import datetime
from django.utils import timezone
import datetime

class Jugadores(models.Model):
	nombre = models.CharField(max_length=30, default='')
	edad = models.IntegerField()	
	posicion = models.CharField(max_length=15, default='')
	foto = models.ImageField(upload_to='apk/static/imagen', verbose_name = 'foto', default = None)
	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	pos = models.IntegerField(default=1)
	nombre = models.CharField(max_length=20, default='')
	puntos = models.IntegerField(default=0)
	GF = models.IntegerField(default=0)
	GC = models.IntegerField(default=0)
	plantilla = models.ManyToManyField(Jugadores)
	def __str__(self):
		return self.nombre

class Partidos(models.Model):
	dia = models.DateField()
	resultado = models.CharField(max_length=10, default='0  -  0')
	local = models.ForeignKey(Equipo, related_name='local')
	visitante = models.ForeignKey(Equipo, related_name='visitante')
	arbitro = models.CharField(max_length=20, default='')
	def __str__(self):
		return self.arbitro


