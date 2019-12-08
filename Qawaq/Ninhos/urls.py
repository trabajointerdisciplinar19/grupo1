from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'Ninhos'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name = 'registro'),
    #path('usuario/login/', views.login,name = 'login'),
    path('usuario/', include('django.contrib.auth.urls')),
    path('Cuentos/<int:id>/',views.cuento, name= 'cuento'),
]
