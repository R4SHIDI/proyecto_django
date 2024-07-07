# Generated by Django 5.0.6 on 2024-07-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_marca_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=250, verbose_name='Fecha')),
                ('nombre', models.CharField(max_length=250, verbose_name='Rut')),
                ('Monto', models.CharField(max_length=250, verbose_name='Monto')),
            ],
        ),
    ]