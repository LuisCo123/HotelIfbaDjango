"""HotelIFBA URL Configuration

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
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from HotelariaIFBA.api import viewsets
# Empresa, ListaDeServico, TipoServico,Empregados,
# Cliente,Reserva,Alojamento,ServicosUtilizados

router = routers.DefaultRouter()
router.register(r'empresa', viewsets.EmpresaViewSet)
router.register(r'listadeservico', viewsets.ListaDeServicoViewSet)
router.register(r'tiposervico', viewsets.TipoServicoViewSet)
router.register(r'empregados', viewsets.EmpregadosViewSet)
router.register(r'cliente', viewsets.ClienteViewSet)
router.register(r'reserva', viewsets.ReservaViewSet)
router.register(r'alojamento', viewsets.AlojamentoViewSet)
router.register(r'servicosutilizados', viewsets.ServicosUtilizadosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
