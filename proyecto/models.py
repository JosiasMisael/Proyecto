from django.db import models 

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
                verbose_name="Pais"
                verbose_name_plural="Paises"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100) 
    imagen = models.ImageField()
    Pais = models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
                verbose_name="Autor"
                verbose_name_plural="Autores"
                ordering = ["-nombre"]
    def __str__(self):
        return self.nombre
  
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    editoria = models.CharField(max_length=100)
    unidad  = models.IntegerField()
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=3)
    publicacion = models.IntegerField(null=True)
    image = models.ImageField(blank=True, null=True, verbose_name="imagen")
    autor = models.ManyToManyField(Autor)
    def __str__(self):
        return self.titulo



