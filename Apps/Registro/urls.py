from django.urls import path
from . import views

urlpatterns = [   #Conjunto de rutas
    path('', views.home),
    path('registrarEmpresa/',views.registrarEmpresa),
    path('edicionEmpresa/<nit>', views.edicionEmpresa),
    path('editarEmpresa/', views.editarEmpresa),
    path('eliminarEmpresa/<nit>', views.eliminarEmpresa)
]