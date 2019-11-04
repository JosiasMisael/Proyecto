from django.contrib import admin
from  .models import Libro, Pais, Autor, Categoria, AutorAdmin, LibroAdmin

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Pais)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
