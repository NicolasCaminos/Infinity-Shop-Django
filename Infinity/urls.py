"""
URL configuration for Infinity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls import handler404, handler500
from AppInfinity.views import pagina_no_encontrada, error_servidor

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('AppInfinity.urls')),
     path('', include('accounts.urls')),
    # Esta línea configura el manejador de error 404
    re_path(r'^.*/$', pagina_no_encontrada, name='pagina_no_encontrada'),
]

if settings.DEBUG:
   
    handler500 = error_servidor
else:
    handler500 = 'AppInfinity.views.error_servidor'
  
