from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'TI-PagPrinc/index.html')

def registro(request):
    return render(request, 'TI2-Registro/Registro.html')

def pag_login(request):
    return render(request, 'Login/login.html')

def login(request):
    pass
