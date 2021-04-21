from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#Pagina princiapl
def index(request):
    return render (request,'diverty/index.html')

#formulario login
def formulario_login(request):
    return render (request,'diverty/formulario_login.html')
#formulario register
def formulario_register(request):
    return render (request,'diverty/formulario_register.html')

#crud clientes
def crud_clientes(request):
    return render (request,'diverty/crud_clientes.html')
#crud reservas
def crud_reservas(request):
    return render (request,'diverty/crud_reservas.html')
#formulario reservas
def formulario_reservas(request):
    return render (request,'diverty/formulario_reservas.html')
#crud empleado
def crud_empleado(request):
    return render (request,'diverty/crud_empleado.html')
#formulario empleado
def formulario_empleado(request):
    return render (request,'diverty/formulario_empleado.html')

#crud ventas
def crud_ventas(request):
    return render (request,'diverty/crud_ventas.html')
#formulario ventas
def formulario_ventas(request):
    return render (request,'diverty/formulario_ventas.html')

#crud promociones
def crud_promociones(request):
    return render (request,'diverty/crud_promociones.html')
#formulario promociones
def formulario_promociones(request):
    return render (request,'diverty/formulario_promociones.html')
#crud atracciones
def crud_atracciones(request):
    return render (request,'diverty/crud_atracciones.html')
#formulario atracciones
def formulario_atracciones(request):
    return render (request,'diverty/formulario_atracciones.html')
def crud_detalles(request):
    return render (request,'diverty/crud_detalles.html')
