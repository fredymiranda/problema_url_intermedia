from urllib import request
from django.shortcuts import render
from AppIntermedia.models import *
from AppIntermedia.forms import *
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, "AppIntermedia/inicio.html")



def crearSucursales(request):
    if request.method == "POST":
        formulario = CrearSucursal(request.POST)
        if formulario.is_valid():
            datosIngresados = formulario.cleaned_data
            sucursal = Sucursal(pais = datosIngresados["paisF"], ciudad = datosIngresados["ciudadF"], direccion = datosIngresados["direccionF"], codigoSucursal = datosIngresados["codigoSucursalF"], correoSucursal = datosIngresados["correoSucursalF"])
            sucursal.save()
            nuevoFormulario = CrearSucursal()
            return render(request, "AppIntermedia/crearSucursales.html", {"formulario":nuevoFormulario})
    else:
        formulario = CrearSucursal()
    return render(request, "AppIntermedia/crearSucursales.html", {"formulario":formulario})



def crearServicios(request):
    if request.method == "POST":
        formulario = CrearServicio(request.POST)
        if formulario.is_valid():
            datosIngresados = formulario.cleaned_data
            servicio = Servicio(codigoServicio = datosIngresados["codigoServicioF"], nombreServicio = datosIngresados["nombreServicioF"], descripcionServicio = datosIngresados["descripcionServicioF"], unidadFacturacion = datosIngresados["unidadFacturacionF"], costoUnidad = datosIngresados["costoUnidadF"])
            servicio.save()
            nuevoFormulario = CrearServicio()
            return render(request, "AppIntermedia/crearServicios.html", {"formulario":nuevoFormulario})
    else:
        formulario = CrearServicio()
    return render(request, "AppIntermedia/crearServicios.html", {"formulario":formulario})



def crearEmpleados(request):
    if request.method == "POST":
        formulario = CrearEmpleado(request.POST)
        if formulario.is_valid():
            datosIngresados = formulario.cleaned_data
            empleado = Empleado(nombres = datosIngresados["nombresF"], apellidos = datosIngresados["apellidosF"], codigoEmpleado = datosIngresados["codigoEmpleadoF"], numeroIdentificacion = datosIngresados["numeroIdentificacionF"], correo = datosIngresados["correoF"])
            empleado.save()
            nuevoFormulario = CrearEmpleado()
            return render(request, "AppIntermedia/crearEmpleados.html", {"formulario":nuevoFormulario})
    else:
        formulario = CrearEmpleado()
    return render(request, "AppIntermedia/crearEmpleados.html", {"formulario":formulario})


"""
def consultarSucursales(request):
    if request.method == "GET":
        busqueda = request.GET("ciudadFormulario")
        return render(request, "AppIntermedia/consultarSucursales.html",)
    else:
        return render(request, "AppIntermedia/consultarSucursales.html",)
"""

def consultarSucursales(request):
    return render(request,"AppIntermedia/consultarSucursales.html")

def resultadosSucursales(request):
    if request.GET["ciudadFormulario"]:
        ciudadBuscada = request.GET["ciudadFormulario"]
        sucursales = Sucursal.objects.filter(ciudad__iexact=ciudadBuscada)
        return render(request,"AppIntermedia/consultarSucursales.html",{"ciudad":ciudadBuscada,"sucursales":sucursales})
    else:
        mensaje = "No ingresaste datos para consultar"
    return render(request,"AppIntermedia/consultarSucursales.html",{"mensaje":mensaje})

#De acuerdo al ejemplo en clase
#Borrar
def busquedaSucursales(request):
    return render(request,"AppIntermedia/busquedaSucursales.html")

#De acuerdo al ejemplo en clase
#Borrar
def buscar(request):
    if request.GET["pais"]:
        busqueda = request.GET["pais"]
        sucursales = Sucursal.objects.filter(pais__iexact=busqueda)
        return render(request,"AppIntermedia/resultados.html",{"sucursal":sucursales,"buscado":busqueda})
    else:
        mensaje = "No enviaste datos"
    return HttpResponse(mensaje)



def consultarServicios(request):
    return render(request, "AppIntermedia/consultarServicios.html")



def consultarEmpleados(request):
    return render(request, "AppIntermedia/consultarEmpleados.html")
