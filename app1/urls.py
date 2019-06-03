from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='principal'),
    path('complejo', views.complejoAdmin, name='view_Complejo'),
    path('complejo/actualizar', views.complejoUpdate, name='update_Complejo'),
]
