from django.contrib import admin
from .models import Accesorio, TipoUsuario, Usuario

# Register your models here.

admin.site.register(Accesorio)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)