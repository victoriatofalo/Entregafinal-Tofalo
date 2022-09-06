from ast import For
from http.client import HTTPResponse
from typing import List
from urllib import request
from django.shortcuts import render,HttpResponse,redirect
from comercio.models import Productos,RegistroMayoristas,Sorteo
from authentication.models import Avatar
from comercio.forms import FormularioBusqueda,FormularioMayoristas
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    avatar = Avatar.objects.filter(user = request.user).first()

    listado_productos= Productos.objects.all()

    if request.GET.get("nombre_producto"):
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos= Productos.objects.filter(nombre__icontains = data["nombre_producto"])
            
            return render(request,"comercio/index.html",{"productos": listado_productos,"formulario":formulario,"imagen":avatar.imagen.url})
       
    else:
        formulario = FormularioBusqueda()
        return render(request,"comercio/index.html",{"productos": listado_productos, "formulario":formulario,"imagen":avatar.imagen.url})

@login_required   
def crear_mayorista(request):
    
    if request.method =="GET":
        return render(request,"comercio/formulario_mayorista.html")
    else:
        nombre = request.POST["nombre"]
        empresa = request.POST["empresa"]
        correo = request.POST["correo"]
        mayoristas =RegistroMayoristas(nombre=nombre,empresa=empresa,correo=correo)
        mayoristas.save()
        return redirect("mayoristas")

class ProductosList(ListView):
    model = Productos
    template_name = "comercio/productos_list.html"

class ProductosDetail(DetailView):
    model = Productos
    template_name = "comercio/productos_detail.html"
class ProductosCreate(LoginRequiredMixin, CreateView):
    model = Productos
    success_url = "/comercio/productos/"
    fields = ["nombre","material","precio"]

class ProductosUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    success_url = "/comercio/productos/"
    fields = ["nombre","material","precio"]

class ProductosDelete(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = "/comercio/productos/"

def quienes_somos(request):
    return render(request,"comercio/quienes_somos.html")

class MayoristasView(ListView):
    model = RegistroMayoristas
    template_name = "comercio/mayoristas_list.html"

class MayoristasDetail(DetailView):
    model = RegistroMayoristas
    template_name = "comercio/mayoristas_detail.html"

class MayoristasUpdate(LoginRequiredMixin, UpdateView):
    model = RegistroMayoristas
    success_url = "/comercio/listado_mayorista/"
    fields = ["nombre","empresa","correo"]

class MayoristasDelete(LoginRequiredMixin, DeleteView):
    model = RegistroMayoristas
    success_url = "/comercio/listado_mayorista/"




    



