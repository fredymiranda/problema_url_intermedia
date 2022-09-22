from django.urls import path
from AppIntermedia.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Crear/Sucursales', crearSucursales, name='CrearSucursales'),
    path('Crear/Empleados', crearEmpleados, name='CrearEmpleados'),
    path('Crear/Servicios', crearServicios, name='CrearServicios'),
    path('Consulta/Sucursales/', consultarSucursales, name='ConsultarSucursales'),
    path('Consulta/Empleados', consultarEmpleados, name='ConsultarEmpleados'),
    path('Consulta/Servicios', consultarServicios, name='ConsultarServicios'),
    path('Consulta/Sucursales/Resultados/', resultadosSucursales),
    #path('Resultados/Sucursales',consultarSucursales), #Borrar
    #path('ConsultarSucursales/',busquedaSucursales, name='ConsultarSucursales'), #Borrar
    path('buscar/',buscar), #Borrar
]