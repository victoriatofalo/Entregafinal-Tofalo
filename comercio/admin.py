from atexit import register
from django.contrib import admin
from comercio.models import *
# Register your models here.
admin.site.register(Productos)
admin.site.register(RegistroMayoristas)
admin.site.register(Sorteo)