"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
schema_view = get_swagger_view(title="Swagger Docs")
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('account/', include('customaccount.api_urls')),
    path('products/', include('products.api_urls')),
    path('sitesetting/', include('sitesetting.api_urls')),
    path('ticket/', include('ticket.api_urls')),
    path('newsletter/', include('news.api_urls')),
    path('auth/', include('auth.api_urls')),
    path('api-token-auth', views.obtain_auth_token),
    path('auth/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('order/', include('order.api_urls')),
    path('orderp/', include('order.urls')),
    path('api/admin/', include('panneladmin.api_url')),

    # Schema - Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
