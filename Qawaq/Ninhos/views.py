from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .utils import *
from django.contrib.auth.decorators import login_required, permission_required
from .models import *

def index(request):
    if request.user.is_authenticated:
        values = {}
        values['username'] = request.user.get_username()
        libros = Material_Aprendizaje.objects.all()[:4]
        sufijo_1 = "titulo"
        sufijo_2 = "imagen"
        sufijo_3 = "descripcion"
        sufijo_4 = "id"
        for i in range(len(libros)):
            values[sufijo_1+str(i)] = libros[i].titulo
            values[sufijo_4+str(i)] = libros[i].id
            valor = (str(libros[i].imagen)).split('/')
            values[sufijo_2+str(i)] = valor[1]+'/'+valor[2]+'/'+valor[3]
            values[sufijo_3+str(i)] = libros[i].descripcion
        return render(request,'PaginaIniciada/index.html',values)
    else:
        return render(request,'TI-PagPrinc/index.html')

def registro(request):
    if request.method == 'POST':
        F_nombre = request.POST['P_nombre']
        S_nombre = request.POST['S_nombre']
        P_Apellido = request.POST['P_Apellido']
        S_Apellido = request.POST['S_Apellido']
        Sexo = request.POST['sexo']
        Nacimiento = request.POST['Nacimiento']
        username = request.POST['username']
        password = request.POST['password']
        agregar_user(username,password)
        agregar_usuario(F_nombre, S_nombre,P_Apellido,S_Apellido,Sexo,Nacimiento)
        agregar_webuser(F_nombre, S_nombre,P_Apellido,S_Apellido,username)
        return redirect(reverse('Ninhos:login'));
    else:
        return render(request, 'TI2-Registro/Registro.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            return render(request,'PaginaIniciada/index.html')
        else:
            return render(request,'registration/login.html')
    else:
        return render(request,'registration/login.html')

def logout(request):
    logout(request)
    return(redirect(reverse('Ninhos:login')))

@login_required
def cuento(request, id):
    extra = {}
    extra['username'] = request.user.get_username()
    data = Material_Aprendizaje.objects.get(id=id)
    extra['libro'] = Libro.objects.get(Material_Apren=data)
    extra['Apredizaje'] = data
    valor = (str(data.imagen)).split('/')
    extra['imagen01'] = "../../"+valor[1]+'/'+valor[2]+'/'+valor[3]
    return render(request,'PaginaIniciada/Cuentos/Cuentos.html',extra)

@login_required
def pregunta(request, id):
    extra = {}
    extra['username'] = request.user.get_username()
    if request.method == 'POST':
        cantidad_lineas = get_number_lineas(id)
        respondido = []
        for i in range(cantidad_lineas):
            value = request.POST["Preg"+str(i)]
            value = value[:len(value)-2]
            respondido.append(value)
        extra['puntuacion'] = comparar(id, respondido,cantidad_lineas)
        agregar_puntuacion(request.user.id, id, extra['puntuacion'])
        return render(request, 'PaginaIniciada/Cuentos/puntuacion.html',extra)

    else:
        extra['Preguntas'] = get_preguntas(id)
        return render(request,'PaginaIniciada/Cuentos/Preguntas.html',extra)
