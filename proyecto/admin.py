from django.contrib import admin
from  .models import Libro, Pais, Autor, Categoria

# Register your models here.

admin.site.register(Libro)
admin.site.register(Pais)
admin.site.register(Autor)
admin.site.register(Categoria)
