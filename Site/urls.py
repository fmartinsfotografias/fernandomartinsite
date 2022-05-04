from django.urls import path

from . import views

# 1º parametro(Rota), 2° parametro (views), 3ºparamentro(namespace)
urlpatterns = [
    path('', views.index, name='index'),
    path('whatsapp', views.py_automacao_whatapp, name='whatsapp')
]