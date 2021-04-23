from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import  promociones,atracciones,clientes,ventas,reserva,detalles,Empleado,Usuario
# Create your views here.

#Pagina princiapl
def index(request):
    return render (request,'diverty/index.html')

#formulario login
def formulario_login(request):
    return render (request,'diverty/formulario_login.html')
#formulario register
def formulario_register(request):
    return render (request,'diverty/formulario_clientes.html')

"""Lógica de clientes """

def crud_clientes(request):

    usuarios=clientes.objects.all()
    contexto={"Usuarios":usuarios}
    return render (request,'diverty/crud_clientes.html',contexto)
#Gurdado de clientes
def guardarClientes(request):
    if request.method=="POST":
        nom=request.POST["nombre"]
        apell=request.POST["apellido"]
        age=request.POST["edad"]
        calle=request.POST["direccion"]
        numero=request.POST["telefono"]
        guardado=clientes(nombre=nom,apellido=apell,edad=age,direccion=calle,telefono=numero)
        guardado.save()
        return HttpResponseRedirect(reverse('diverty:crud_clientes',args=()))
    else:
        return HttpResponse("fin")
#Eliminar Clientes
def eliminarClientes(request,id):
    borrado=clientes.objects.get(pk=id)
    borrado.delete()
    return HttpResponseRedirect(reverse('diverty:crud_clientes',args=()))

def actualizarClientes(request,id):
    actualizacion = clientes.objects.get(pk = id)
    contexto = { 'datos': actualizacion }
    return render(request, 'diverty/actualizar_clientes.html', contexto)

def editarClientes(request):
    if request.method=="POST":
        id=request.POST['id']
        nom=request.POST['nombre']
        apelli=request.POST['apellido']
        age=request.POST['edad']
        dire=request.POST['direccion']
        telef=request.POST['telefono']
        edicion_clientes=clientes.objects.get(pk=id)
        edicion_clientes.nombre=nom
        edicion_clientes.apellido=apelli
        edicion_clientes.edad=age
        edicion_clientes.direccion=dire
        edicion_clientes.telefono=telef
        edicion_clientes.save()#Actualizar
        return HttpResponseRedirect(reverse('diverty:crud_clientes',args=()))
    else:
        HttpResponse('fin')
"""Fin lógica de clientes"""

#crud reservas
def crud_reservas(request):
    return render (request,'diverty/crud_reservas.html')
#formulario reservas
def formulario_reservas(request):
    return render (request,'diverty/formulario_reservas.html')

"""Lógica de empleado"""

def crud_empleado(request):
    empleados=Empleado.objects.all()
    contexto={"Empleado":empleados}
    return render (request,'diverty/crud_empleado.html',contexto)

def guardarEmpleado(request):
    if request.method=="POST":
        nom=request.POST['nombre']
        apelli=request.POST['apellido']
        iden=request.POST['identificacion']
        email=request.POST['correo']
        guardado=Empleado(nombre=nom,apellido=apelli,identificacion=iden,correo=email)
        guardado.save()
        return HttpResponseRedirect(reverse('diverty:crud_empleado',args=()))
    else:
        HttpResponse("fin")
def eliminarEmpleado(request,id):
    borrado=Empleado.objects.get(pk=id)
    borrado.delete()
    return HttpResponseRedirect(reverse('diverty:crud_empleado',args=()))

def actualizarEmpleado(request,id):
    actualizacion=Empleado.objects.get(pk=id)
    contexto={'actualizarEmpleado':actualizacion}
    return render (request,'diverty/actualizar_empleado.html',contexto)

def editarEmpleado(request):
    if request.method=="POST":
        id=request.POST['id']
        nom=request.POST['nombre']
        ape=request.POST['apellido']
        iden=request.POST['identificacion']
        email=request.POST['correo']
        edicion_empleados=Empleado.objects.get(pk=id)
        edicion_empleados.nombre=nom
        edicion_empleados.apellido=ape
        edicion_empleados.identificacion=iden
        edicion_empleados.correo=email
        edicion_empleados.save()#actualizar
        return HttpResponseRedirect(reverse('diverty:crud_empleado',args=()))
    else:
        HttpResponse("fin")   

""" Fin logica de empleados"""

#crud ventas
def crud_ventas(request):
    ventas_boletas=ventas.objects.all()
    contexto={'items_ventas':ventas_boletas}
    
    return render (request,'diverty/crud_ventas.html',contexto)

def guardarVentas(request):
    if request.method=="POST":
        c=clientes.objects.get(pk=request.POST["cliente"])
        q=ventas(
            fecha= request.POST["fecha"],
            costo=request.POST["costo"],
            clientes=c

        )
        
        q.save()
        return HttpResponseRedirect(reverse('diverty:crud_ventas'),args=())
    else:
        HttpResponse("fin")

  
#formulario empleado
def formulario_empleado(request):
    return render (request,'diverty/formulario_empleado.html')


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
