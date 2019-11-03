from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)

    class Meta:
                verbose_name="Pais"
                verbose_name_plural="Paises"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre
   
class Libro(models.Model):
    encargado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    editoria = models.CharField(max_length=100)
    unidad  = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=3)
    publicacion = models.IntegerField(null=True)
    image = models.ImageField(blank=True, verbose_name="imagen")
    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100) 
    Pais = models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
                verbose_name="Autor"
                verbose_name_plural="Autores"
                ordering = ["-nombre"]
    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre

