# Generated by Django 3.1.7 on 2021-05-01 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('cuit', models.CharField(max_length=15)),
                ('comentarios', models.TextField(blank=True, default='Sin comentarios', null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Situacion_frente_iva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(blank=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de venta')),
                ('descripcion', models.TextField(blank=True, default='Sin descripcion')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activo', models.BooleanField(default=True)),
                ('barriles', models.ManyToManyField(to='produccion.Barril')),
                ('cliente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='ventas.cliente')),
                ('forma_de_pago', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='ventas.forma_de_pago')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='situacion_frente_iva',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='ventas.situacion_frente_iva'),
        ),
    ]
