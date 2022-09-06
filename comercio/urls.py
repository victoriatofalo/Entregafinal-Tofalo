from django.urls import path
from comercio.views import *

urlpatterns = [
    path("buscar_producto/", index, name="inicio"),
    path("quienes_somos/",quienes_somos,name="quienes_somos"),
    path("mayoristas/",crear_mayorista, name="mayoristas"),
    path('productos/',ProductosList.as_view(),name="productos"),
    path('productos/crear/',ProductosCreate.as_view(),name = "productos_crear"),
    path('productos/actualizar/<pk>',ProductosUpdate.as_view(),name = "productos_update"),
    path('productos/borrar/<pk>',ProductosDelete.as_view(),name = "productos_delete"),
    path('productos/<pk>',ProductosDetail.as_view(),name="productos_detail"),
    path('listado_mayorista/',MayoristasView.as_view(),name="listado_mayorista"),
    path('listado_mayorista/<pk>',MayoristasDetail.as_view(),name="mayoristas_detail"),
    path('listado_mayorista/editar/<pk>',MayoristasUpdate.as_view(),name = "mayoristas_update"),
    path('listado_mayorista/borrar/<pk>',MayoristasDelete.as_view(),name = "mayoristas_delete"),

    
    
]