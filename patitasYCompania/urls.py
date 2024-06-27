from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.product_list, name='product_list'),
    path('producto/<int:product_id>/', views.product_detail, name='product_detail'),
    path('producto/crear/', views.product_create, name='product_create'),
    path('producto/<int:product_id>/editar/', views.product_update, name='product_update'),
    path('producto/<int:product_id>/eliminar/', views.product_delete, name='product_delete'),
    path('contacto/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('perfil/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('api/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('api/get_cart/', views.get_cart, name='get_cart'),
]
