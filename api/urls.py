from django.urls import include, path
from rest_framework import routers
from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'complejos', views.ComplejoViewSet)
router.register(r'canchas', views.CanchaViewSet, basename='canchas')
router.register(r'reservas', views.ReservaViewSet, basename='reservas')
router.register(r'suscripcion', views.SuscripcionViewSet, basename='suscripciones')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]