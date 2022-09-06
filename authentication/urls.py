from atexit import register
from django.urls import path
from authentication.views import *

urlpatterns = [
    path("login/",login_view,name="login"),
    path("logout/",logout_view,name="logout"),
    path("registro/",register_view,name="registro"),
    path("editar_usuario/",editar_usuario,name="editar_usuario"),
    path("avatar/",agregar_avatar,name="agregar_avatar"),
    path("perfil/",perfil,name="perfil"),
    path('mensajes/',MensajesList.as_view(),name="mensajes"),
    path('mensajes/crear/',MensajesCreate.as_view(),name = "mensajes_crear"),

    
    
]