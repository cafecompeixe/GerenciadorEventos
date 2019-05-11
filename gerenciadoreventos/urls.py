"""gerenciadoreventos URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from core.api.viewsets import EventoViewSet, SobreViewSet
from atividade.api.viewsets import AtividadeViewSet
from endereco.api.viewsets import EnderecoViewSet
from presenca.api.viewsets import PresencaViewSet


router = routers.DefaultRouter()
router.register(r'sobre', SobreViewSet)
router.register(r"eventos",EventoViewSet)
router.register(r"atividades",AtividadeViewSet)
router.register(r"endereco",EnderecoViewSet)
router.register(r"presenca",PresencaViewSet)
urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include(router.urls))

]
