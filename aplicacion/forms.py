from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RecetaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la receta", max_length=50, required=True)
    ingredientes = forms.CharField(label="Ingredientes", max_length=50, required=True)
    tiempo = forms.IntegerField(label="Tiempo de preparación en minutos", required=True)
    DIFICULTAD = (
        (1, "Fácil"),
        (2, "Media"),
        (3, "Difícil"),
    )
    dificultad = forms.ChoiceField(
        label="Dificultad", choices=DIFICULTAD, required=True
    )
    imagen_url = forms.CharField(
        label="URL de la imagen", max_length=200, required=True
    )


class CocineroForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cocinero", max_length=50, required=True)
    apellido = forms.CharField(
        label="Apellido del cocinero", max_length=50, required=True
    )
    edad = forms.IntegerField(label="Edad", required=True)
    especialidad = forms.CharField(label="Especialidad del cocinero", max_length=50)
    anios_experiencia = forms.IntegerField(label="Años de experiencia", required=True)
    email = forms.CharField(label="Email", max_length=50, required=True)
    telefono = forms.CharField(
        label="Teléfono del contacto", max_length=50, required=True
    )


class RestauranteForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre del restaurante", max_length=50, required=True
    )
    direccion = forms.CharField(label="Dirección", max_length=50, required=True)
    telefono = forms.CharField(
        label="Teléfono del contacto", max_length=50, required=True
    )
    CATEGORIA = (
        ("Comida rápida", "Comida rápida"),
        ("Meriendas", "Meriendas"),
        ("Veggie", "Veggie"),
        ("Cena", "Cena"),
    )
    categoria = forms.ChoiceField(label="Categoría", choices=CATEGORIA, required=True)
    envio_domilicio = forms.BooleanField(label="¿Envío a domicilio?", required=False)
    CALIFICACIONES = (
        (1, "A mejorar"),
        (2, "Regular"),
        (3, "Bueno"),
        (4, "Muy bueno"),
        (5, "Excelente"),
    )
    calificacion = forms.ChoiceField(
        label="Calificación", choices=CALIFICACIONES, required=True
    )
    capacidad = forms.IntegerField(label="Capacidad", required=True)
    eventos = forms.BooleanField(label="¿Eventos?", required=False)


class ProveedorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del proveedor", max_length=50, required=True)
    telefono = forms.CharField(
        label="Teléfono del contacto", max_length=50, required=True
    )
    email = forms.CharField(label="Email", max_length=50, required=True)
    PRODUCTO = (
        ("Carnes", "Carnes"),
        ("Verdura", "Verdura"),
        ("Bebidas", "Bebidas"),
        ("Pescado", "Pescado"),
        ("Postres", "Postres"),
        ("Pan", "Pan"),
    )
    producto = forms.ChoiceField(label="Producto", choices=PRODUCTO, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    sitio_web = forms.CharField(label="Sitio web", max_length=50, required=True)
    METODOS_PAGO = (
        ("Efectivo", "Efectivo"),
        ("Tarjeta", "Tarjeta"),
        ("Transferencia", "Transferencia"),
        ("Todos", "Todos"),
    )
    metodos_pago = forms.ChoiceField(
        label="Métodos de pago", choices=METODOS_PAGO, required=True
    )
    entrega_inmediata = forms.BooleanField(label="¿Entrega inmediata?", required=False)


class UsuarioCreacionForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=50, required=True)
    password1 = forms.CharField(
        label="Contraseña", max_length=50, required=True, widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        max_length=50,
        required=True,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {k: "" for k in fields}


class UsuarioEdicionForm(UserChangeForm):
    email = forms.EmailField(label="Email", max_length=50, required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)
    password = None

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Avatar", required=True)
