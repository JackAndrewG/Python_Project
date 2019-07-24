
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API`S')
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('app1.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	path('api/', include('api.urls')),
    url(r'^documentacion/', schema_view)
]
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
