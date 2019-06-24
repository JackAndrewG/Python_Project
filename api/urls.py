from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=True)
router.register(r'users', UserViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]