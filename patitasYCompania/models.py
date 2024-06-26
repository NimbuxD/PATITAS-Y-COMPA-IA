from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    disponible = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("can_create_accesorio", "Puede crear accesorios"),
            ("can_edit_accesorio", "Puede editar accesorios"),
            ("can_delete_accesorio", "Puede eliminar accesorios"),
        ]

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, related_name='usuarios')
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Cambiar el nombre relacionado
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Cambiar el nombre relacionado
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.groups.exists():  # Si el usuario no tiene grupo asignado
            if self.tipo_usuario.nombre == 'Administrador':
                admin_group, created = Group.objects.get_or_create(name='Administrador')
                if created:
                    content_type = ContentType.objects.get_for_model(Accesorio)
                    permissions = Permission.objects.filter(content_type=content_type)
                    admin_group.permissions.set(permissions)
                self.groups.add(admin_group)
            elif self.tipo_usuario.nombre == 'Cliente':
                cliente_group, created = Group.objects.get_or_create(name='Cliente')
                if created:
                    content_type = ContentType.objects.get_for_model(Accesorio)
                    view_permission = Permission.objects.get(codename='view_accesorio', content_type=content_type)
                    cliente_group.permissions.add(view_permission)
                self.groups.add(cliente_group)
