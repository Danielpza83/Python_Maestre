from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),


#Paths de HTML
    path('peliculas/', peliculas, name="peliculas"),
    path('clientes/', clientes, name="clientes"),
    path('videojuegos/', videojuegos, name="videojuegos"),

#Paths de Forms
    path('videojuegosForm/', videojuegosForm, name="videojuegosForm"),
    path('clientesForm/', clientesForm, name="clientesForm"),
    path('peliculasForm/', peliculasForm, name="peliculasForm"),

#Paths de Buscadores
    path('buscarPelicula/', buscarPelicula, name="buscarPelicula"),
    path('buscarVideojuegos/', buscarVideojuegos, name="buscarVideojuegos"),
    path('buscarConsolas/', buscarConsolas, name="buscarConsolas"),
    path('buscarClientes/', buscarClientes, name="buscarClientes"),
    path('buscarNombre/', buscarNombre, name="buscarNombre"),
    path('buscar/', buscar, name="buscar"),

#Edit-Delete
    path('updateClientes/<id_clientes>/', updateClientes, name="updateClientes"),
    path('deleteClientes/<id_clientes>', deleteClientes, name="deleteClientes"),
    path('updateVideojuegos/<id_videojuegos>/', updateVideojuegos, name="updateVideojuegos"),
    path('deleteVideojuegos/<id_videojuegos>', deleteVideojuegos, name="deleteVideojuegos"),
    path('updatePeliculas/<id_peliculas>/', updatePeliculas, name="updatePeliculas"),
    path('deletePeliculas/<id_peliculas>', deletePeliculas, name="deletePeliculas"),



#Login - Logout - Register - Edit Profile
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', register, name="register"),
    path('editProfile/', editProfile, name='editProfile'),
    path('addAvatar/', addAvatar, name='addAvatar'),

#AboutMe Page
    path('aboutme/', aboutme, name="aboutme"),

]