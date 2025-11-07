"""
URL configuration for ActividadesRealizar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from autenticacion import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('recuperarContrasena/', views.recuperarContrasena, name='recuperarContrasena'),
    path('tareas/', views.listarTareas, name='listarTareas'),
    path('crearTarea/', views.crearTarea, name='crearTarea'),
    path('informacionTarea/<int:idTarea>/', views.informacionTarea, name='informacionTarea'),
    path('eliminarTarea/<int:idTarea>/', views.eliminarTarea, name='eliminarTarea'),
]
