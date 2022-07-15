from django.db import models

# Create your models here.
class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True)
    nombreImagen=models.CharField(max_length=250)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    precio=models.CharField(max_length=100)
    def __str__(self):
        return self.nombreImagen