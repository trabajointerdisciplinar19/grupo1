from .models import *
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import *
import calendar
from django.contrib.auth.models import User
from decimal import *

class Pregunta_extra:
    def __init__(self):
        self.question = ""
        self.alternativas = []
        self.id = 0



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


def get_preguntas(id):
    pregunta_valores = Pregunta.objects.get(Evaluacion=Material_Aprendizaje.objects.get(id=id))
    archivo = open(pregunta_valores.Preguntas,"r")
    preguntas = []
    cant_preguntas = int(archivo.readline())
    for i in range(cant_preguntas):
        helper = Pregunta_extra()
        helper.id = "Preg"+str(i)
        helper.question = archivo.readline()
        alternativas = int((archivo.readline()))
        juntar = []
        for j in range(alternativas):
            juntar.append((archivo.readline()))

        #print(juntar)
        helper.alternativas = juntar
        preguntas.append(helper)
    archivo.close()
    return preguntas


def get_number_lineas(id):
    respuesta = Pregunta.objects.get(Evaluacion=Material_Aprendizaje.objects.get(id=id))
    archivo = open(respuesta.Respuestas,"r")
    answer = len(archivo.readlines())
    archivo.close()
    return answer


def comparar(id, marcado, cantidad):
    respuesta = Pregunta.objects.get(Evaluacion=Material_Aprendizaje.objects.get(id=id))
    archivo = open(respuesta.Respuestas,"r")
    errores = 0
    puntuacion_ind = 100 / cantidad
    for estado in range(cantidad):
        line = archivo.readline()
        line = line[:len(line)-1]
        #print (line + " " + marcado[estado])
        if line != marcado[estado]:
            errores+=1

    archivo.close()
    return round(100 - errores * puntuacion_ind)


def agregar_puntuacion(id_user, id_apren, puntuacion):
    dato = Historial()
    dato.user = Usuario.objects.get(user= User.objects.get(id=id_user))
    dato.material_a = Material_Aprendizaje.objects.get(id = id_apren)
    dato.resultado = puntuacion
    dato.fecha_realizada = date.today()
    dato.save()
