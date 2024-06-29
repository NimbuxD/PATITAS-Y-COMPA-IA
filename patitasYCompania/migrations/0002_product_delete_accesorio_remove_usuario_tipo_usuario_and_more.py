# Generated by Django 5.0.6 on 2024-06-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patitasYCompania', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.DeleteModel(
            name='Accesorio',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]