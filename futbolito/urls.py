"""futbolito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view
# from api.urls import *

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

schema_view = get_swagger_view(title='API`S')
urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('app1.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	# url(r'^apis/', include(('api.u', 'api'), namespace='hola')),
	# url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^documentacion/', schema_view)
]