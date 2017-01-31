from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^equipo$', views.ver_equipo, name='equipos'),
    url(r'^clasificacion$', views.ver_clasificacion, name='clasificaciones'),
    url(r'jugadores/equipo/(?P<pk>\d+)/$', views.ver_jugadores_equipo, name='jugadores'),
    url(r'^partidos$',views.ver_jornada, name='partidos')
]