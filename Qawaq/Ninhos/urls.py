from django.urls import path

from . import views

app_name = 'Ninhos'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name = 'registro'),
    path('login/', views.pag_login, name = 'pag_login'),
]
