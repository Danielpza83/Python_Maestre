from django.db import models
from django.contrib.auth.models import User

# Create your models here.

generos_peliculas = (
    ("DRAMA", "Drama"),
    ("ACCION", "Acción"),
    ("AVENTURA", "Aventura"),
    ("COMEDIA", "Comedia"),
    ("TERROR", "Terror"),
    ("OTROS", "Otros"),
 )

generos_videojuegos = (
    ("FPS", "FPS"),
    ("ACCION", "Acción"),
    ("AVENTURA", "Aventura"),
    ("ESTRATEGIA", "Estrategia"),
    ("TERROR", "Terror"),
    ("OTROS", "Otros"),
    )

consolas = (
    ("PLAYSTATION_4", "PlayStation 4"),
    ("PLAYSTATION_5", "PlayStation 5"),
    ("NINTENDO_SWITCH", "Nintendo Switch"),
    ("XBOX_ONE", "Xbox One"),
    ("PC", "PC"),
    ("OTROS", "Otros"),
)


class Peliculas(models.Model):
    
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    productora = models.CharField(max_length=50)
    actor_protagonista = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=generos_peliculas)
    fecha_estreno = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.titulo}"


class Videojuegos(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    productora = models.CharField(max_length=50)
    actor_protagonista = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=generos_videojuegos)
    fecha_estreno = models.DateField()
    cantidad = models.IntegerField()
    consolas = models.CharField(max_length=20, choices=consolas)

    def __str__(self):
        return f"{self.titulo}, ({self.consolas})"

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Avatar(models.Model):
    image = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.image}]"
