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
    path('actualizar_clientes/<int:id>/', views.actualizarClientes, name='actualizar_clientes'),
    path('editar_clientes/',views.editarClientes,name='editar_clientes'),
    #Fin clientes
    

    path ('crud_reservas/',views.crud_reservas,name='crud_reservas'),
    path('formulario_reservas/',views.formulario_reservas,name='formulario_reservas'),

        #empleados urls:
    path('crud_empleado/',views.crud_empleado,name='crud_empleado'),
    path('guardar_empleado/',views.guardarEmpleado, name='guardar_empleado'),
    path('eliminar_empleado/<int:id>/', views.eliminarEmpleado,name='eliminar_empleado'),
    path('actualizar_empleado/<int:id>/',views.actualizarEmpleado,name='actualizar_empleado'),
    path('editar_empleado',views.editarEmpleado,name="editar_empleado"),

    #fin empleados
    path('formulario_empleado/',views.formulario_empleado,name='formulario_empleado'),

    path('crud_ventas/',views.crud_ventas,name='crud_ventas'),
    #ventas urls
    path('formulario_ventas/',views.formulario_ventas,name='formulario_ventas'),
    path('guardar-ventas',views.guardarVentas,name='guardar-ventas'),

    
    path('crud_promociones/',views.crud_promociones,name='crud_promociones'),
    path('formulario_promociones/',views.formulario_promociones,name='formulario_promociones'),
    path('crud_atracciones/',views.crud_atracciones,name='crud_atracciones'),
    path('formulario_atracciones/',views.formulario_atracciones,name='formulario_atracciones'),
    path('crud_detalles/',views.crud_detalles,name='crud_detalles')
   
]

