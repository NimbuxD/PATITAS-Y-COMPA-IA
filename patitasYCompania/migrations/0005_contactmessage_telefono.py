# Generated by Django 5.0.6 on 2024-06-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patitasYCompania', '0004_producto_usuario_delete_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
