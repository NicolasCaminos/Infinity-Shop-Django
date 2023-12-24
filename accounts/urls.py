from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import editar_request, login_request, register_request, home,logout_view

urlpatterns = [
    path('register/', register_request, name="register"),
    path('editar/', editar_request, name="editar"),
    path('login/', login_request, name="login"),
    path('home/', home, name="home"),
    path('logout/',logout_view, name="logout"),
    
    ]
