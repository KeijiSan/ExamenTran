# Generated by Django 4.0.6 on 2022-07-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreImagen', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.CharField(max_length=100)),
            ],
        ),
    ]