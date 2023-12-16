from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Auth
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Views
from django.views.generic import UpdateView, DeleteView
from django.views.generic.detail import DetailView


def index(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        recetas = Receta.objects.filter(nombre__contains=nombre)
        ctx = {"recetas": recetas}

        if not recetas:
            ctx = {"error": "No se encontraron recetas con ese nombre"}

        return render(request, "aplicacion/index.html", ctx)

    ctx = {"recetas": Receta.objects.all()}

    return render(request, "aplicacion/index.html", ctx)


def acerca_de_mi(request):
    return render(request, "aplicacion/acerca-de-mi.html")


# Recetas
@login_required
def recetas(request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            ingredientes = form.cleaned_data["ingredientes"]
            tiempo = form.cleaned_data["tiempo"]
            dificultad = form.cleaned_data["dificultad"]
            imagen_url = form.cleaned_data["imagen_url"]

            Receta.objects.create(
                nombre=nombre,
                ingredientes=ingredientes,
                tiempo=tiempo,
                dificultad=dificultad,
                imagen_url=imagen_url,
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = RecetaForm()

    ctx = {"recetas": Receta.objects.all(), "form": form}

    return render(request, "aplicacion/recetas/recetas.html", ctx)


class RecetaDelete(LoginRequiredMixin, DeleteView):
    model = Receta
    nombre = "la receta"
    url = "recetas"
    success_url = reverse_lazy("recetas")
    template_name = "aplicacion/eliminar.html"


class RecetaUpdate(LoginRequiredMixin, UpdateView):
    model = Receta
    nombre = "receta"
    url = "recetas"
    fields = ["nombre", "ingredientes", "tiempo", "dificultad", "imagen_url"]
    success_url = reverse_lazy("recetas")
    template_name = "aplicacion/editar.html"


class RecetaDetail(DetailView):
    model = Receta
    template_name = "aplicacion/recetas/detalle_receta.html"


# Cocineros
@login_required
def cocineros(request):
    if request.method == "POST":
        form = CocineroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            edad = form.cleaned_data["edad"]
            especialidad = form.cleaned_data["especialidad"]
            anios_experiencia = form.cleaned_data["anios_experiencia"]
            email = form.cleaned_data["email"]
            telefono = form.cleaned_data["telefono"]

            Cocinero.objects.create(
                nombre=nombre,
                apellido=apellido,
                edad=edad,
                especialidad=especialidad,
                anios_experiencia=anios_experiencia,
                email=email,
                telefono=telefono,
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = CocineroForm()

    ctx = {"cocineros": Cocinero.objects.all(), "form": form}
    return render(request, "aplicacion/cocineros/cocineros.html", ctx)


class CocineroDelete(LoginRequiredMixin, DeleteView):
    model = Cocinero
    nombre = "el cocinero"
    url = "cocineros"
    success_url = reverse_lazy("cocineros")
    template_name = "aplicacion/eliminar.html"


class CocineroUpdate(LoginRequiredMixin, UpdateView):
    model = Cocinero
    nombre = "cocinero"
    url = "cocineros"
    fields = [
        "nombre",
        "apellido",
        "edad",
        "especialidad",
        "anios_experiencia",
        "email",
        "telefono",
    ]
    success_url = reverse_lazy("cocineros")
    template_name = "aplicacion/editar.html"


class CocineroDetail(LoginRequiredMixin, DetailView):
    model = Cocinero
    template_name = "aplicacion/cocineros/detalle_cocinero.html"


# Restaurantes
@login_required
def restaurantes(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            direccion = form.cleaned_data["direccion"]
            telefono = form.cleaned_data["telefono"]
            categoria = form.cleaned_data["categoria"]
            envio_domilicio = form.cleaned_data["envio_domilicio"]
            calificacion = form.cleaned_data["calificacion"]
            capacidad = form.cleaned_data["capacidad"]
            eventos = form.cleaned_data["eventos"]

            Restaurante.objects.create(
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                categoria=categoria,
                envio_domilicio=envio_domilicio,
                calificacion=calificacion,
                capacidad=capacidad,
                eventos=eventos,
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = RestauranteForm()

    ctx = {"restaurantes": Restaurante.objects.all(), "form": form}
    return render(request, "aplicacion/restaurantes/restaurante.html", ctx)


class RestauranteDelete(LoginRequiredMixin, DeleteView):
    model = Restaurante
    nombre = "el restaurante"
    url = "restaurantes"
    success_url = reverse_lazy("restaurantes")
    template_name = "aplicacion/eliminar.html"


class RestauranteUpdate(LoginRequiredMixin, UpdateView):
    model = Restaurante
    nombre = "restaurant"
    url = "restaurantes"
    fields = [
        "nombre",
        "direccion",
        "telefono",
        "categoria",
        "envio_domilicio",
        "calificacion",
        "capacidad",
        "eventos",
    ]
    success_url = reverse_lazy("restaurantes")
    template_name = "aplicacion/editar.html"


class RestauranteDetail(LoginRequiredMixin, DetailView):
    model = Restaurante
    template_name = "aplicacion/restaurantes/detalle_restaurante.html"


# Proveedores
@login_required
def proveedores(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            telefono = form.cleaned_data["telefono"]
            email = form.cleaned_data["email"]
            producto = form.cleaned_data["producto"]
            localidad = form.cleaned_data["localidad"]
            sitio_web = form.cleaned_data["sitio_web"]
            metodos_pago = form.cleaned_data["metodos_pago"]
            entrega_inmediata = form.cleaned_data["entrega_inmediata"]

            Proveedor.objects.create(
                nombre=nombre,
                telefono=telefono,
                email=email,
                producto=producto,
                localidad=localidad,
                sitio_web=sitio_web,
                metodos_pago=metodos_pago,
                entrega_inmediata=entrega_inmediata,
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = ProveedorForm()

    ctx = {"proveedores": Proveedor.objects.all(), "form": form}
    return render(request, "aplicacion/proveedores/proveedores.html", ctx)


class ProveedorDelete(LoginRequiredMixin, DeleteView):
    model = Proveedor
    nombre = "el proveedor"
    url = "proveedores"
    success_url = reverse_lazy("proveedores")
    template_name = "aplicacion/eliminar.html"


class ProveedorUpdate(LoginRequiredMixin, UpdateView):
    model = Proveedor
    nombre = "proveedor"
    url = "proveedores"
    fields = [
        "nombre",
        "telefono",
        "email",
        "producto",
        "localidad",
        "sitio_web",
        "metodos_pago",
        "entrega_inmediata",
    ]
    success_url = reverse_lazy("proveedores")
    template_name = "aplicacion/editar.html"


class ProveedorDetail(LoginRequiredMixin, DetailView):
    model = Proveedor
    template_name = "aplicacion/proveedores/detalle_proveedor.html"


# Login
def logueo(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "https://t4.ftcdn.net/jpg/05/49/98/39/360_F_549983970_bRCkYfk0P6PP5fKbMhZMIb07mCJ6esXL.jpg"
                finally:
                    request.session["avatar"] = avatar

                return redirect("inicio")

            else:
                return render(
                    request,
                    "aplicacion/sesion/login.html",
                    {"error": "Usuario o contraseña incorrectos", "form": form},
                )
        else:
            return render(
                request,
                "aplicacion/sesion/login.html",
                {"error": "Usuario o contraseña incorrectos", "form": form},
            )

    form = AuthenticationForm()
    return render(request, "aplicacion/sesion/login.html", {"form": form})


def registro(request):
    if request.method == "POST":
        form = UsuarioCreacionForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            return render(
                request, "aplicacion/sesion/usuario-creado.html", {"user": user}
            )
    else:
        form = UsuarioCreacionForm()

    return render(request, "aplicacion/sesion/registro.html", {"form": form})


@login_required
def edicion_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UsuarioEdicionForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.email = informacion["email"]
            usuario.save()
            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = UsuarioEdicionForm(
            initial={
                "first_name": usuario.first_name,
                "last_name": usuario.last_name,
                "email": usuario.email,
            }
        )

    return render(request, "aplicacion/sesion/editar-perfil.html", {"form": form})


@login_required
def cambio_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "aplicacion/sesion/editar-perfil.html", {"form": form})


@login_required
def modificacion_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = AvatarForm()
    return render(request, "aplicacion/sesion/edit-avatar.html", {"form": form})
