from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
