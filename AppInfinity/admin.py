from django.contrib import admin
from .models import *

if not admin.site.is_registered(Categoria):
    admin.site.register(Categoria)

# Asegúrate de que Trekking y Comments estén registrados solo una vez
if not admin.site.is_registered(Trekking):
    admin.site.register(Trekking)

if not admin.site.is_registered(Comments):
    admin.site.register(Comments)
    
if not admin.site.is_registered(Cliente):
    admin.site.register(Cliente)

if not admin.site.is_registered(Avatar):
    admin.site.register(Avatar)

if not admin.site.is_registered(Producto):
    admin.site.register(Producto)