from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('complejo/update', views.complejo_update, name='complejo_update'),
    path('cancha', views.cancha, name='cancha'),
    path('cancha/nueva/', views.cancha_nueva, name='cancha_nueva'),
    path('cancha/<int:pk>/editar/', views.cancha_editar, name='cancha_enlace'),
    path('reserva', views.reserva, name='reserva'),
    path('reserva/<int:pk>/editar/', views.reserva_editar, name='reserva_enlace'),
    path('reserva/nueva/', views.reserva_nueva, name='reserva_nueva'),
]
