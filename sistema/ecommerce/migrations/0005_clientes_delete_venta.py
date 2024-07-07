# Generated by Django 5.0.6 on 2024-07-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_venta_rename_mensaje_contacto_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=225)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]