# Generated by Django 4.1 on 2022-09-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=35)),
                ('apellidos', models.CharField(max_length=35)),
                ('codigoEmpleado', models.IntegerField()),
                ('numeroIdentificacion', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoServicio', models.IntegerField()),
                ('nombreServicio', models.CharField(max_length=50)),
                ('descripcionServicio', models.CharField(max_length=200)),
                ('unidadFacturacion', models.CharField(max_length=20)),
                ('costoUnidad', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=120)),
                ('codigoSucursal', models.IntegerField()),
                ('correoSucursal', models.EmailField(max_length=254)),
            ],
        ),
    ]
