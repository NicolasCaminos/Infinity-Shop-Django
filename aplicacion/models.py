from django.db import models
from django.contrib.auth.models import User


class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
    tiempo = models.IntegerField()
    DIFICULTAD = (
        (1, "Fácil"),
        (2, "Media"),
        (3, "Difícil"),
    )
    dificultad = models.IntegerField(choices=DIFICULTAD)
    imagen_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.nombre


class Cocinero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=50)
    anios_experiencia = models.IntegerField()
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    CATEGORIA = (
        ("Comida rápida", "Comida rápida"),
        ("Meriendas", "Meriendas"),
        ("Veggie", "Veggie"),
        ("Cena", "Cena"),
    )
    categoria = models.CharField(max_length=50, choices=CATEGORIA)
    envio_domilicio = models.BooleanField()
    CALIFICACIONES = (
        (1, "A mejorar"),
        (2, "Regular"),
        (3, "Bueno"),
        (4, "Muy bueno"),
        (5, "Excelente"),
    )
    calificacion = models.IntegerField(choices=CALIFICACIONES)
    capacidad = models.IntegerField()
    eventos = models.BooleanField()

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    PRODUCTO = (
        ("Carnes", "Carnes"),
        ("Verdura", "Verdura"),
        ("Bebidas", "Bebidas"),
        ("Pescado", "Pescado"),
        ("Postres", "Postres"),
        ("Pan", "Pan"),
    )
    producto = models.CharField(max_length=50, choices=PRODUCTO)
    localidad = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=50)
    METODOS_PAGO = (
        ("Efectivo", "Efectivo"),
        ("Tarjeta", "Tarjeta"),
        ("Transferencia", "Transferencia"),
        ("Todos", "Todos"),
    )
    metodos_pago = models.CharField(max_length=50, choices=METODOS_PAGO)
    entrega_inmediata = models.BooleanField()

    def __str__(self):
        return self.nombre + " - " + self.producto


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"
