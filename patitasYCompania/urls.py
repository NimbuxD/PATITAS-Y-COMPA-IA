from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('accesorios', views.listar_accesorios, name='lista_accesorios'),
]