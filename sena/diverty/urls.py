from django.urls import path

from.import  views
app_name='diverty'
urlpatterns=[
    
    path('',views.index,name='index'),
     path('formulario_login/',views.formulario_login,name='formulario_login'),
    path('formulario_register/',views.formulario_register,name='formulario_register'),
    #clientes-urls:
    path('crud_clientes/',views.crud_clientes,name='crud_clientes'),
    path('guardar-clientes',views.guardarClientes,name='guardar-clientes'),
    path('eliminar-clientes/<int:id>/',views.eliminarClientes,name='eliminar-clientes'),

    path ('crud_reservas/',views.crud_reservas,name='crud_reservas'),
    path('formulario_reservas/',views.formulario_reservas,name='formulario_reservas'),
    path('crud_empleado/',views.crud_empleado,name='crud_empleado'),
    path('formulario_empleado/',views.formulario_empleado,name='formulario_empleado'),
    path('crud_ventas/',views.crud_ventas,name='crud_ventas'),
    path('formulario_ventas/',views.formulario_ventas,name='formulario_ventas'),
    path('crud_promociones/',views.crud_promociones,name='crud_promociones'),
    path('formulario_promociones/',views.formulario_promociones,name='formulario_promociones'),
    path('crud_atracciones/',views.crud_atracciones,name='crud_atracciones'),
    path('formulario_atracciones/',views.formulario_atracciones,name='formulario_atracciones'),
    path('crud_detalles/',views.crud_detalles,name='crud_detalles')
   
]

