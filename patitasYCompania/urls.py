from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.product_list, name='product_list'),
    path('producto/<int:product_id>/', views.product_detail, name='product_detail'),
    path('producto/crear/', views.product_create, name='product_create'),
    path('producto/<int:product_id>/editar/', views.product_update, name='product_update'),
    path('producto/<int:product_id>/eliminar/', views.product_delete, name='product_delete'),
    path('contacto/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.user_login, name='login'),
    path('perfil/', views.user_profile, name='user_profile'),
    path('logout/', views.user_logout, name='logout'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
