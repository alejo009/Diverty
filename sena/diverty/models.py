from django.db import models


# Create your models here.
 
class promociones(models.Model):
    id_promocion=models.AutoField(primary_key=True)
    fecha=models.DateTimeField(null=False,blank=False,max_length=254)
    def __str__(self):
        return str(self.id_promocion)
   
    

class atracciones (models.Model):
    id_atraccion=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=254,blank=False,null=False)
    capacidad=models.SmallIntegerField(blank=False,null=False)
    fecha=models.DateTimeField(null=False,blank=False,max_length=254)
    precio=models.DecimalField(null=False,blank=False,decimal_places=10,max_digits=250,)
    reserva=models.CharField(max_length=254,blank=False,null=False)
    promociones=models.ForeignKey(promociones,on_delete=models.DO_NOTHING)
    def __str__(self) :
        return str(self.nombre)
   
class clientes(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=254,blank=False,null=False)
    apellido=models.CharField(max_length=254,blank=False,null=False)
    edad=models.SmallIntegerField(null=True,blank=True)
    direccion=models.CharField(max_length=150,blank=False )
    telefono=models.CharField(max_length=15,blank=False,null=False)
    def __str__(self):
        return 'el nombre es %s '  % (self.nombre)
class ventas(models.Model):
    id_venta=models.AutoField(primary_key=True)
    fecha=models.DateTimeField(null=False,blank=False,max_length=254)
    costo=models.DecimalField(null= False,blank=False,decimal_places=10,max_digits=250)
    clientes=models.ForeignKey(clientes,on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id_venta)
    

class reserva(models.Model):
    id_reserva=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=254,blank=False,null=False)
    fecha=models.DateTimeField(null=False,blank=False)
    atracciones_reservas=models.ForeignKey(atracciones,on_delete=models.DO_NOTHING,related_name="%(class)s_atracciones")
    def __str__(self) :
        return str(self.nombre)

class detalles (models.Model):
    detalles_id_ventas=models.ForeignKey(ventas,on_delete=models.DO_NOTHING)
    detalles_id_atraccion=models.ForeignKey(atracciones,on_delete=models.DO_NOTHING)
    costo_ventas=models.DecimalField(blank=False,null=False,decimal_places=10,max_digits=250)
    cantidad=models.CharField(max_length=254,blank=False,null=False)
    total_pagar=models.DecimalField(blank=False,null=False,decimal_places=10,max_digits=250)
    def __str__(self) :
        return str(self.detalles_id_ventas)


class Empleado(models.Model):
    id_empleado=models.AutoField(primary_key=True)
    identificacion = models.IntegerField(unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    apellido = models.CharField(max_length=100,null=False,blank=False)
    correo = models.EmailField(max_length=200)
    def __str__(self) :
        return str(self.nombre)


class Usuario(models.Model):
    ROL = (
        (1,'Administrador'),
        (2,'Empleado'),
        (3,'Cliente'),
    )
    id=models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=200,null=False,blank=False)
    clave = models.CharField(max_length=254,blank=False,null=False)
    rol=models.IntegerField(choices=ROL,default=3)
    def __str__(self) :

        return str(self.rol)