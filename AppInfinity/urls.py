from django.shortcuts import redirect
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/', index, name='index'),
    path('categoria/', categorias, name='categoria'),
    path('ver_categoria/<int:categoria_id>/', ver_categoria, name='ver_categoria'),
    path('eliminar_categoria/<int:categoria_id>/', eliminar_categoria, name='eliminar_categoria'),
    path('producto/', productos, name='producto'),
    path('cliente/', clientes, name='cliente'),
    path('ver_cliente/<int:cliente_id>/', ver_cliente, name='ver_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', eliminar_cliente, name='eliminar_cliente'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
    path('', lambda request: redirect('index/'), name='inicio'),  
    path('about/', about, name='about'),
    path('home/', include('accounts.urls')),
    path('producto/<int:pk>', ProductoDetalleView.as_view(), name="ProductoDetail"),
    path('editar_producto/<int:pk>', EditarProductoView.as_view(), name='editar_producto'),
    path('trekking/', TrekkingView.as_view(), name='trekking_list'),
    path('trekking/<int:trekking_id>/', TrekkingDetailView.as_view(), name='trekking_detail'),
    path('trekking/<int:trekking_id>/save_comment/', save_comment, name='save_comment'),
    path('crear-reporte/', crear_reporte, name='crear_reporte'),
    path("editar-perfil/", edicion_perfil, name="editar_perfil"),
    path("cambiar-password/", cambio_pass, name="cambiar_password"),
    path("agregar-avatar", modificacion_avatar, name="agregar_avatar"),
    path('crear-producto/', crear_producto, name='crear_producto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
