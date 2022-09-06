from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from authentication.forms import EdicionUsuario,UserEditForm,AvatarForm
from django.contrib.auth.decorators import login_required
from authentication.models import Avatar,Mensajes
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def login_view(request):
    if request.method == "GET":
        formulario = AuthenticationForm()
        return render(request,"authentication/login.html",{"form":formulario})
    else:
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username=data["username"],password=data["password"])
            if user is not None:
                login(request,user)
                return redirect("inicio")
        return render(request,"authentication/login.html",{"form":formulario,"error":"Usuario o contraseña incorrecta."})

def register_view(request):
    if request.method =="GET":
        formulario = EdicionUsuario()
        return render(request,"authentication/registro.html",{"form":formulario})
    else:
        formulario = EdicionUsuario(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request,"authentication/registro.html",{"form":formulario})

def logout_view(request):
    logout(request)
    return redirect("inicio")
        
@login_required
def editar_usuario(request):
    if request.method =="GET":
        form = UserEditForm(initial={"email":request.user.email,"first_name":request.user.first_name,"last_name":request.user.last_name})
        return render(request,"authentication/editar_usuario.html",{"form":form})
    else:
        form = UserEditForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            usuario = request.user
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.save()
            return redirect("inicio")
        return render(request,"authentication/editar_usuario.html",{"form":form})

@login_required
def agregar_avatar(request):
    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form":form}
        return render (request,"authentication/agregar_avatar.html",contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            usuario = User.objects.filter(username = request.user.username).first()
            avatar = Avatar(user = usuario, imagen = data["imagen"])
            avatar.save()
            return redirect("inicio")

class MensajesCreate(LoginRequiredMixin, CreateView):
    model = Mensajes
    success_url = "/auth/mensajes/"
    fields = ["usuario","mensaje"]

class MensajesList(ListView):
    model = Mensajes
    template_name = "authentication/lista_mensajes.html"

@login_required
def perfil(request):
    return render(request,"authentication/mi_perfil.html")
