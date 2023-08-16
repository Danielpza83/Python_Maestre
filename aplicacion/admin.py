from django.contrib import admin
from .models import Clientes, Peliculas, Videojuegos, Avatar

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Peliculas)
admin.site.register(Videojuegos)
admin.site.register(Avatar)

