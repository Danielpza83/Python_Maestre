from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html", )

def peliculas(request):
    ctx = {"peliculas": Peliculas.objects.all() }
    return render(request, "aplicacion/peliculas.html", ctx)

def videojuegos(request):
    ctx = {"videojuegos": Videojuegos.objects.all() }
    return render(request, "aplicacion/videojuegos.html", ctx)

def clientes(request):
    ctx = {"clientes": Clientes.objects.all() }
    return render(request, "aplicacion/clientes.html", ctx)

def aboutme(request):
    return render(request, "aplicacion/aboutme.html")

# Forms:

def videojuegosForm(request):
    if request.method == "POST":
        videojuegos_Form = VideojuegosForm(request.POST)
        print(videojuegos_Form)
        if videojuegos_Form.is_valid:
            informacion = videojuegos_Form.cleaned_data
            videojuegos = Videojuegos(
                titulo=informacion['titulo'],
                director=informacion['director'],
                productora=informacion['productora'],
                genero=informacion['genero'],
                fecha_estreno=informacion['fecha_estreno'],
                cantidad=informacion['cantidad'],
                consolas=informacion['consolas'],
            )
            videojuegos.save()
            ctx = {"videojuegos": Videojuegos.objects.all() }
            return render(request, "aplicacion/videojuegos.html", ctx)
    else:
        videojuegos_Form = VideojuegosForm()
        return render(request, "aplicacion/videojuegosForm.html", {"form":videojuegos_Form})

def clientesForm(request):
    if request.method == "POST":
        clientes_Form = ClientesForm(request.POST)
        print(clientes_Form)
        if clientes_Form.is_valid:
            informacion = clientes_Form.cleaned_data
            clientes = Clientes(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                direccion=informacion['direccion'],
            )
            clientes.save()
            ctx = {"clientes": Clientes.objects.all() }
            return render(request, "aplicacion/clientes.html", ctx)
    else:
        clientes_Form = ClientesForm()
        return render(request, "aplicacion/clientesForm.html", {"form":clientes_Form})

def peliculasForm(request):
    if request.method == "POST":
        peliculas_Form = PeliculasForm(request.POST)
        print(peliculas_Form)
        if peliculas_Form.is_valid:
            informacion = peliculas_Form.cleaned_data
            peliculas = Peliculas(
                titulo=informacion['titulo'],
                director=informacion['director'],
                productora=informacion['productora'],
                actor_protagonista=informacion['actor_protagonista'],
                genero=informacion['genero'],
                fecha_estreno=informacion['fecha_estreno'],
                cantidad=informacion['cantidad'],
            )
            peliculas.save()
            ctx = {"peliculas": Peliculas.objects.all() }
            return render(request, "aplicacion/peliculas.html", ctx)
    else:
        peliculas_Form = PeliculasForm()
        return render(request, "aplicacion/peliculasForm.html", {"form":peliculas_Form})
    

#Buscadores

def buscarPelicula(request):
    return render(request, "aplicacion/buscarPelicula.html")

def buscarVideojuegos(request):
    return render(request, "aplicacion/buscarVideojuegos.html")

def buscarClientes(request):
    return render(request, "aplicacion/buscarClientes.html")

def buscar(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        genero = Peliculas.objects.filter(titulo__icontains=titulo)
        return render(request, "aplicacion/resultadosPeliculas.html", 
                      {"titulo":titulo, 
                      "genero":genero}
                      )
    return render(request, "aplicacion/buscarPelicula.html")

def buscarConsolas(request):
    if request.GET['consolas']:
        consolas=request.GET['consolas']
        videojuegos = Videojuegos.objects.filter(consolas__icontains=consolas)
        return render(request, "aplicacion/resultadosVideojuegos.html",
                      {"consolas":consolas,
                       "videojuegos":videojuegos}
                      )
    return render(request, "aplication/buscarVideojuegos.html")

def buscarNombre(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        clientes= Clientes.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadosClientes.html",
                      {"nombre":nombre,
                       "clientes":clientes}
                       )
    return render(request, "aplicacion/buscarClientes.html")


#Edit - Delete

@login_required
def updateClientes(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    if request.method == "POST":
        editclientes = EditClientesForm(request.POST)
        if editclientes.is_valid():
            clientes.nombre = editclientes.cleaned_data.get('nombre')
            clientes.apellido = editclientes.cleaned_data.get('apellido')
            clientes.email = editclientes.cleaned_data.get('email')
            clientes.direccion  = editclientes.cleaned_data.get('direccion')
            clientes.save()
            return redirect(reverse_lazy('clientes'))
    else:
        clientes_Form = ClientesForm(initial={'nombre':clientes.nombre,
                                              'apellido':clientes.apellido,
                                              'email':clientes.email,
                                              'direccion':clientes.direccion})
    return render(request, "aplicacion/clientesForm.html", {"form":clientes_Form})

@login_required
def updateVideojuegos(request, id_videojuegos):
    videojuegos = Videojuegos.objects.get(id=id_videojuegos)
    if request.method == "POST":
        editvideojuegos = EditVideojuegosForm(request.POST)
        if editvideojuegos.is_valid():
            videojuegos.titulo = editvideojuegos.cleaned_data.get('titulo')
            videojuegos.director = editvideojuegos.cleaned_data.get('director')
            videojuegos.productora = editvideojuegos.cleaned_data.get('productora')
            videojuegos.genero = editvideojuegos.cleaned_data.get('genero')
            videojuegos.fecha_estreno = editvideojuegos.cleaned_data.get('fecha_estreno')
            videojuegos.cantidad = editvideojuegos.cleaned_data.get('cantidad')
            videojuegos.consolas = editvideojuegos.cleaned_data.get('consolas')
            videojuegos.save()
            return redirect(reverse_lazy('videojuegos'))
    else:
        videojuegos_Form = VideojuegosForm(initial={'titulo':videojuegos.titulo,
                                              'director':videojuegos.director,
                                              'productora':videojuegos.productora,
                                              'genero':videojuegos.genero,
                                              'fecha_estreno':videojuegos.fecha_estreno,
                                              'cantidad':videojuegos.cantidad,
                                              'consolas':videojuegos.consolas})
    return render(request, "aplicacion/videojuegosForm.html", {"form":videojuegos_Form})

@login_required
def updatePeliculas(request, id_peliculas):
    peliculas = Peliculas.objects.get(id=id_peliculas)
    if request.method == "POST":
        editpeliculas = EditPeliculasForm(request.POST)
        if editpeliculas.is_valid():
            peliculas.titulo = editpeliculas.cleaned_data.get('titulo')
            peliculas.director = editpeliculas.cleaned_data.get('director')
            peliculas.productora = editpeliculas.cleaned_data.get('productora')
            peliculas.actor_protagonista = editpeliculas.cleaned_data.get('actor_protagonista')
            peliculas.genero = editpeliculas.cleaned_data.get('genero')
            peliculas.fecha_estreno = editpeliculas.cleaned_data.get('fecha_estreno')
            peliculas.cantidad = editpeliculas.cleaned_data.get('cantidad')
            peliculas.save()
            return redirect(reverse_lazy('peliculas'))
    else:
        peliculas_Form = PeliculasForm(initial={'titulo':peliculas.titulo,
                                              'director':peliculas.director,
                                              'productora':peliculas.productora,
                                              'actor_protagonista':peliculas.actor_protagonista,
                                              'genero':peliculas.genero,
                                              'fecha_estreno':peliculas.fecha_estreno,
                                              'cantidad':peliculas.cantidad})
    return render(request, "aplicacion/peliculasForm.html", {"form":peliculas_Form})

@login_required
def deleteClientes(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    clientes.delete()
    return redirect(reverse_lazy('clientes'))

@login_required
def deleteVideojuegos(request, id_videojuegos):
    videojuegos = Videojuegos.objects.get(id=id_videojuegos)
    videojuegos.delete()
    return redirect(reverse_lazy('videojuegos'))

@login_required
def deletePeliculas(request, id_peliculas):
    peliculas = Peliculas.objects.get(id=id_peliculas)
    peliculas.delete()
    return redirect(reverse_lazy('peliculas'))


# Login - Logout - Registration

def login_request(request):
    if request.method == "POST":
        authForm = AuthenticationForm(request, data=request.POST)
        if authForm.is_valid():
            usuario = authForm.cleaned_data.get('username')
            clave = authForm.cleaned_data.get('password')
            user = authenticate(username= usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatars/default.png'
                finally:
                    request.session['avatar'] = avatar


                
                return render(request, "aplicacion/base.html")
            else:
                return render(request, "aplicacion/login.html", {"mensaje": f"Datos Inválidos", "form":authForm})
        else:
            return render(request, "aplicacion/login.html", {"mensaje": f"Datos Inválidos", "form":authForm})
           
    else:
        authForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form":authForm})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})
    else:
        form = UserCreationForm()

    return render(request, "aplicacion/registro.html", {"form": form})

@login_required
def editProfile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data.get('email')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return render(request, "aplicacion/base.html", {'mensaje2': f"Usuario {user.username} se ha actualizado correctamente"})
        else:
            return render(request, "aplicacion/editProfile.html", {"form": form})
    else:
        form = UserEditForm(instance=user)
    return render(request, "aplicacion/editProfile.html", {"form": form})
    

#Avatar
@login_required
def addAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            OldAvatar = Avatar.objects.filter(user=u)
            if len(OldAvatar) > 0: 
                OldAvatar[0].delete()
            avatar = Avatar(user=u, image=form.cleaned_data['image'])
            avatar.save()
            image = Avatar.objects.get(user=request.user.id).image.url
            request.session['avatar'] = image

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarForm()
        return render(request, "aplicacion/addAvatar.html", {"form": form})
