from django.urls import path

from . import views

# 1┬║ parametro(Rota), 2┬░ parametro (views), 3┬║paramentro(namespace)
urlpatterns = [
    path('', views.index, name='index'),
    path('whatsapp', views.py_automacao_whatapp, name='whatsapp')
]