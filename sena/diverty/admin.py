from django.contrib import admin
from .models import  promociones,atracciones,clientes,ventas,reserva,detalles,Empleado,Usuario

class promocionesAdmin(admin.ModelAdmin):
    list_display = ('id_promocion', 'fecha')
    search_fields = ['id_promocion']
admin.site.register(promociones,promocionesAdmin)

class AtraccionesAdmin(admin.ModelAdmin):
    list_display=('id_atraccion','nombre','capacidad','fecha','precio','reserva','promociones')
    list_filter=['promociones']
    search_fields=['id_atraccion','nombre']
admin.site.register(atracciones,AtraccionesAdmin)

class ClientesAdmin(admin.ModelAdmin):
    list_display=('id_cliente','nombre','apellido','edad','direccion','telefono')
   
    search_fields=['id_cliente','nombre']
admin.site.register(clientes,ClientesAdmin  )

class ventasAdmin(admin.ModelAdmin):
    list_display=('id_venta','fecha','costo','clientes')
    search_fields=['clientes','id_venta']
    list_filter=['clientes']
    
admin.site.register(ventas,ventasAdmin)

class reservaAdmin(admin.ModelAdmin):
    list_display=('id_reserva','nombre','fecha','atracciones_reservas')
    search_fields=['atracciones_reservas','id_reserva']
    list_filter = ['atracciones_reservas']

admin.site.register(reserva,reservaAdmin)

class detalleAdmin(admin.ModelAdmin):
    list_display=('detalles_id_ventas','detalles_id_atraccion','costo_ventas','cantidad','total_pagar')
    search_fields=['detalles_id_atraccion','detalles_id_ventas']


admin.site.register(detalles,detalleAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('id_empleado','identificacion','nombre','apellido','correo')
    search_fields=['correo','apellido']

admin.site.register(Empleado,EmpleadoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'clave','rol')

admin.site.register(Usuario, UsuarioAdmin)
# Register your models here.

