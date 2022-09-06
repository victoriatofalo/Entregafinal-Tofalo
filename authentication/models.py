from django.db import models
from django.db.models import CharField,FloatField,EmailField
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatar",default=None,null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add=True,null=True,blank=True)

class Mensajes(models.Model):
    usuario = models.CharField(max_length=80)
    mensaje = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True,null=True,blank=True)