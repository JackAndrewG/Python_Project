from django.urls import include, path
from rest_framework import routers
from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'complejos', views.ComplejoViewSet)
router.register(r'canchas', views.CanchaViewSet, base_name='canchas')
router.register(r'reservas', views.ReservaViewSet, base_name='reservas')
router.register(r'suscripcion', views.SuscripcionViewSet, base_name='suscripciones')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]