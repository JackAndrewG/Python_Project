from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.post_list, name='principal'),
    path('complejo', views.complejoAdmin, name='view_Complejo'),
    path('complejo/actualizar', views.complejoUpdate, name='update_Complejo'),
=======
    path('', views.inicio, name='inicio'),
    path('cancha', views.cancha, name='cancha'),
    path('cancha/nueva/', views.cancha_nueva, name='cancha_nueva'),
    path('cancha/<int:pk>/editar/', views.cancha_editar, name='cancha_enlace'),
    path('reserva', views.reserva, name='reserva'),
    path('reserva/<int:pk>/editar/', views.reserva_editar, name='reserva_enlace'),
    path('reserva/nueva/', views.reserva_nueva, name='reserva_nueva'),
>>>>>>> 8009f5c292c6e19246eeded258f58cb6f00e0595
]
