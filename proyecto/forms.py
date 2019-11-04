from django import forms
from .models import Pais, Categoria, Autor, Libro

class PaisForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del pais'}))
    class Meta:
        model = Pais
        fields = ('nombre',)

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la categoria'}))
    class Meta:
        model = Categoria 
        fields = ('nombre',)

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre','apellido', 'direccion', 'telefono','email','Pais')
class LibroForm(forms.ModelForm):
    class Meta:
        model =  Libro
        fields = ('titulo','editoria','categoria','unidad', 'precio','publicacion','autor')
    
    def __init__ (self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        self.fields["autor"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["autor"].help_text = "Ingrese los Autores"
        self.fields["autor"].queryset = Autor.objects.all()




    