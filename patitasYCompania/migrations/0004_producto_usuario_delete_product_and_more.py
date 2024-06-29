# Generated by Django 5.0.6 on 2024-06-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patitasYCompania', '0003_contactmessage_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='productos/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RenameField(
            model_name='contactmessage',
            old_name='created_at',
            new_name='creado_el',
        ),
        migrations.RenameField(
            model_name='contactmessage',
            old_name='message',
            new_name='mensaje',
        ),
        migrations.RenameField(
            model_name='contactmessage',
            old_name='name',
            new_name='nombre',
        ),
    ]