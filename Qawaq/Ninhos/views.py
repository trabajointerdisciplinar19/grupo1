from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .utils import *


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('Ninhos:login'));
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return render(request,'PaginaIniciada/index.html')
        else:
            return render(request,'registration/login.html')
    else:
        return render(request,'registration/login.html')
