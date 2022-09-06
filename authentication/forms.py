from ast import Pass
from tkinter import Image
from django.forms import Form,CharField,IntegerField,EmailField,PasswordInput,ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authentication.models import Mensajes
from django.forms import ModelForm

class EdicionUsuario(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)
    first_name = CharField(label="Nombre")
    last_name = CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password1","password2"]

class AvatarForm(Form):
    imagen = ImageField()



    

