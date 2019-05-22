from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='principal'),
    path('complejo', views.post_list, name='view_Complejo'),
]
