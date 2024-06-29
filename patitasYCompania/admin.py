from django.contrib import admin
from .models import ContactMessage, Producto, Usuario

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(ContactMessage)
