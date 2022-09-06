from django.db import models
from django.db.models import CharField,FloatField,EmailField
from django.contrib.auth.models import User

class Productos(models.Model):
    nombre =models.CharField(max_length=150)
    material = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"Nombre producto: {self.nombre} - de: {self.material}. Precio: {self.precio}"

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

class RegistroMayoristas(models.Model):
    nombre = models.CharField(max_length=80)
    correo = models.EmailField(max_length=100)
    empresa = models.CharField(blank=True,null=True,max_length=100)
    fecha = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"Empresa: {self.empresa} - Nombre: {self.nombre} - Correo: {self.correo}"
    
    class Meta:
        verbose_name="Mayorista"
        verbose_name_plural="Mayoristas"

class Sorteo(models.Model):
    nombre = models.CharField(max_length=80)
    correo = models.CharField (max_length=80)
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre cliente: {self.nombre} - correo: {self.correo}"

    class Meta:
        verbose_name="Sorteo"
        verbose_name_plural="Sorteos"


