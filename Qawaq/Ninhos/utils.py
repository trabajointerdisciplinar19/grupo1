from .models import *
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import *
import calendar
from django.contrib.auth.models import User

def calculate_edad(Nacimiento):
    ahora = datetime.now()
    d = date(*(int(s) for s in Nacimiento.split('-')))
    diferencia = relativedelta(ahora, d)
    return diferencia.years


def agregar_user(username,password):
    user = User.objects.create_user(username, email=None, password=password)
    user.save()

def agregar_usuario(F_nombre, S_nombre,P_Apellido,S_Apellido,Sexo,Nacimiento):
    dato = Ninho()
    dato.P_Nombre = F_nombre
    dato.S_Nombre = S_nombre
    dato.Apellido_P = P_Apellido
    dato.Apellido_M = S_Apellido
    dato.sexo = Sexo
    dato.fecha_nacimiento = Nacimiento
    dato.edad_mental = calculate_edad(Nacimiento)
    dato.temas_interes = ""
    dato.save()


def agregar_webuser(F_nombre, S_nombre,P_Apellido,S_Apellido,username):
    # NO agrega usuario web -- falla en el get de dato.ninho-- chequear
    dato = Usuario()
    dato.user = User.objects.get(username=username)
    dato.nivel_lectura = 0.00
    #Error era S_Nombre no S_nombre
    dato.ninho = Ninho.objects.get(P_Nombre=F_nombre, S_Nombre=S_nombre, Apellido_P=P_Apellido, Apellido_M=S_Apellido)
    dato.save()
