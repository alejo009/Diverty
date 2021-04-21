from django.shortcuts import render
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

#crud clientes
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


def editarClientes(request):
    pass

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
