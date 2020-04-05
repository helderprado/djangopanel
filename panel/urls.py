"""panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from list.views import home_view, estoque, etiquetada, estampada, verificar_estoque, verificar_etiquetada, verificar_estampada, delete, edit, observacoes, pronta_entrega, verificar_pronta_entrega

urlpatterns = [
	path('', home_view, name='home'),
	path('estoque/<list_id>', estoque, name='estoque'),
    path('etiquetada/<list_id>', etiquetada, name='etiquetada'),
    path('estampada/<list_id>', estampada, name='estampada'),
    path('verificar_estoque/<list_id>', verificar_estoque, name='verificar_estoque'),
    path('verificar_etiquetada/<list_id>', verificar_etiquetada, name='verificar_etiquetada'),
    path('verificar_estampada/<list_id>', verificar_estampada, name='verificar_estampada'),
    path('pronta_entrega/<list_id>', pronta_entrega, name='pronta_entrega'),
    path('verificar_pronta_entrega/<list_id>', verificar_pronta_entrega, name='verificar_pronta_entrega'),
    path('delete/<list_id>', delete, name='delete'),
    path('observacoes/<list_id>', observacoes, name='observacoes'),
    path('edit/<list_id>', edit, name='edit'),
    path('admin/', admin.site.urls),
]
