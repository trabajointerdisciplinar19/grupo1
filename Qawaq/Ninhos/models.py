from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ninho(models.Model):
#    DNI = models.PositiveIntegerField(primary_key = True)
    P_Nombre = models.CharField(max_length = 20)
    S_Nombre = models.CharField(max_length = 20)
    Apellido_P = models.CharField(max_length = 20)
    Apellido_M = models.CharField(max_length = 20)
    sexo = models.CharField(max_length = 1)
    edad_mental = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    temas_interes = models.TextField()


class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nivel_lectura = models.DecimalField(max_digits = 5, decimal_places = 2)
    ninho = models.OneToOneField(Ninho,on_delete=models.PROTECT)


class Material_Aprendizaje(models.Model):
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField()
    dificultad = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="Ninhos/static/Imagenes_BD/")
    tema = models.CharField(max_length = 30)


class Historial(models.Model):
    user = models.OneToOneField(Usuario,on_delete=models.PROTECT)
    material_a = models.OneToOneField(Material_Aprendizaje,on_delete=models.PROTECT)
    resultado = models.PositiveIntegerField()
    fecha_realizada = models.DateField()


class Libro(models.Model):
    isbn = models.PositiveIntegerField()
    genero = models.CharField(max_length = 30)
    autor = models.TextField()
    Material_Apren = models.ForeignKey(Material_Aprendizaje,on_delete = models.CASCADE)


class Videos(models.Model):
    URL = models.URLField()
    duracion = models.DurationField()
    Material_Aprendizaje = models.ForeignKey(Material_Aprendizaje,on_delete = models.CASCADE)


class Pregunta(models.Model):
    Preguntas = models.FilePathField(path="Ninhos/static/Preguntas")
    Respuestas = models.FilePathField(path="Ninhos/static/Respuestas")
    Evaluacion = models.OneToOneField(Material_Aprendizaje,on_delete=models.CASCADE)



"""
class Evaluacion(models.Model):
    puntuacion_total = models.DecimalField(max_digits = 2, decimal_places = 2)
    Material_A = models.ForeignKey(Material_Aprendizaje, on_delete = models.CASCADE)
"""

"""
class Minigame(models.Model):
    Ubicacion = models.FilePathField()
    Solucion = models.FilePathField()
    Evaluacion = models.OneToOneField(Evaluacion,on_delete=models.PROTECT)
"""
