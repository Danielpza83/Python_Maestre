from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClientesForm(forms.Form):
    nombre = forms.CharField(label="Inserte su Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Inserte su Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Inserte su Email", max_length=50, required=True)
    direccion = forms.CharField(label="Inserte su Dirección", max_length=200, required=False)

class PeliculasForm(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=50, required=True)
    director = forms.CharField(label="Director", max_length=50, required=False)
    productora = forms.CharField(label="Productora", max_length=50, required=False)
    actor_protagonista = forms.CharField(label="Protagonista", max_length=50, required=True)
    generos_peliculas = (
        ("DRAMA", "Drama"),
        ("ACCION", "Acción"),
        ("AVENTURA", "Aventura"),
        ("COMEDIA", "Comedia"),
        ("TERROR", "Terror"),
        ("OTROS", "Otros"),
    )
    genero = forms.ChoiceField(label="Genero", choices=generos_peliculas, required=True)
    fecha_estreno = forms.DateField(label="Fecha de Estreno", required=False)
    cantidad = forms.IntegerField(label="Cantidad", required=True)

class VideojuegosForm(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=50, required=True)
    director = forms.CharField(label="Director", max_length=50, required=False)
    productora = forms.CharField(label="Productora", max_length=50, required=False)
    generos_videojuegos = (
        ("FPS", "FPS"),
        ("ACCION", "Acción"),
        ("AVENTURA", "Aventura"),
        ("ESTRATEGIA", "Estrategia"),
        ("TERROR", "Terror"),
        ("OTROS", "Otros"),
        )
    genero = forms.ChoiceField(label="Genero", choices=generos_videojuegos, required=True)
    fecha_estreno = forms.DateField()
    cantidad = forms.IntegerField(label="Cantidad", required=True)
    nombres_consolas = (
        ("PLAYSTATION_4", "PlayStation 4"),
        ("PLAYSTATION_5", "PlayStation 5"),
        ("NINTENDO_SWITCH", "Nintendo Switch"),
        ("XBOX_ONE", "Xbox One"),
        ("PC", "PC"),
        ("OTROS", "Otros"),
        )
    consolas = forms.ChoiceField(label="Consola", choices=nombres_consolas, required=True)


#Edit

class EditClientesForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", max_length=50, required=True)
    direccion = forms.CharField(label="Dirección", max_length=200, required=False)

class EditVideojuegosForm(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=50, required=True)
    director = forms.CharField(label="Director", max_length=50, required=False)
    productora = forms.CharField(label="Productora", max_length=50, required=False)
    generos_videojuegos = (
        ("FPS", "FPS"),
        ("ACCION", "Acción"),
        ("AVENTURA", "Aventura"),
        ("ESTRATEGIA", "Estrategia"),
        ("TERROR", "Terror"),
        ("OTROS", "Otros"),
        )
    genero = forms.ChoiceField(label="Genero", choices=generos_videojuegos, required=True)
    fecha_estreno = forms.DateField()
    cantidad = forms.IntegerField(label="Cantidad", required=True)
    nombres_consolas = (
        ("PLAYSTATION_4", "PlayStation 4"),
        ("PLAYSTATION_5", "PlayStation 5"),
        ("NINTENDO_SWITCH", "Nintendo Switch"),
        ("XBOX_ONE", "Xbox One"),
        ("PC", "PC"),
        ("OTROS", "Otros"),
        )
    consolas = forms.ChoiceField(label="Consola", choices=nombres_consolas, required=True)

class EditPeliculasForm(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=50, required=True)
    director = forms.CharField(label="Director", max_length=50, required=False)
    productora = forms.CharField(label="Productora", max_length=50, required=False)
    actor_protagonista = forms.CharField(label="Protagonista", max_length=50, required=True)
    generos_peliculas = (
        ("DRAMA", "Drama"),
        ("ACCION", "Acción"),
        ("AVENTURA", "Aventura"),
        ("COMEDIA", "Comedia"),
        ("TERROR", "Terror"),
        ("OTROS", "Otros"),
    )
    genero = forms.ChoiceField(label="Genero", choices=generos_peliculas, required=True)
    fecha_estreno = forms.DateField(label="Fecha de Estreno", required=False)
    cantidad = forms.IntegerField(label="Cantidad", required=True)


#Edit Users

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
          model = User
          fields = [ 'email', 'first_name', 'last_name', 'password1', 'password2']
          help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
      image = forms.ImageField(required=True)
      