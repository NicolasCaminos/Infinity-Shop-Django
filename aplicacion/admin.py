from django.contrib import admin
from .models import Cocinero, Receta, Restaurante, Proveedor, Avatar

# Register your models here.
admin.site.register(Cocinero)
admin.site.register(Receta)
admin.site.register(Restaurante)
admin.site.register(Proveedor)
admin.site.register(Avatar)
