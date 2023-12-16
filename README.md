# 👨‍🍳 Recetas de cocina

Web desarrollada en Django con patron MVT.

## 📄 Objetivo funcional:

Webapp permite administrar un modelo de negocio de restaurante y allí poder consultar, crear, modificar y eliminar recetas de cocina, cociner@s, restaurantes (de por ejemplo una red de partners) y proveedores. Cuenta con un registro para que los usuarios puedan hacer CRUD de los modelos. Sin loguearse sólo es posible ver y buscar recetas, eso a fin de que un usuario sin permisos sólo vea las recetas que se ofrecen, pero la parte del negocio propiamiente dicha (como proveedores) sea sólo para usuarios autenticados. Existe un superadmin que a la vez tiene acceso a panel de control (User: admin, Pass: admin). Los conceptos que se tratan son:

- Herencia HTML
- Clases en modelos
- Formularios de ingreso de datos en todas las clases
- CRUD completo
- Relaciones entre clases
- Formulario de búsqueda de recetas por su nombre
- Vistas basadas en Clases

## Particularidades

Para el CRUD, se eligió usar vistas basadas en clases para UpdateView, DeleteView y DetailView, no así para el ListView y CreateView ya que se usaron funciones para poder hacer la carga del modelo instanciado mediante un dialog emergente, por lo que se personalizó mendiante una función.

## Modelos

- Receta
- Cocinero
- Restaurante
- Proveedor
- Avatar (para almacenar la imagen de usuario)

## 🔧 Instalación

1 - Para instalar el proyecto se debe clonar el repositorio 
```
git clone https://github.com/NicolasCaminos/ProyectoFinal.git
```
2 - Instalar Pillow ya que necesitamos manipular imágenes
```
pip install Pillow
```

## Uso

1 - Para utilizar el proyecto se debe ejecutar el siguiente comando en la carpeta del proyecto
```
python manage.py runserver
```

2 - Luego se debe ingresar al localhost en el puerto 8000
<br><br>
`http://127.0.0.1:8000/` o `http://localhost:8000/`

<br>

3 - La pantalla principal de la web muestra la bienvenida, el listado de recetas en formato card y un input de búsqueda, este último permite buscar recetas por su nombre. Si se ingresa un nombre de receta que no existe, se mostrará un mensaje de feedback. Al hacer click en una receta se navegará a su detalle:

<br>

![primero](https://github.com/NicolasCaminos/ProyectoFinal/blob/main/aplicacion/static/aplicacion/assets/primero.gif)



<br><br>

4 - El usuario cuenta con un nav en la parte superior donde puede logearse o bien crear la cuenta en caso que no posea una, al acceder se habilitan las demás secciones. También se puede ingresar a su panel clickeando el avatar para modificar la información.

<br>

![segundo](https://raw.githubusercontent.com/NicolasCaminos/ProyectoFinal-main/main/aplicacion/static/aplicacion/assets/segundo.gif)


<br><br>

5 - Dentro de la modificación de los datos el usuario puede agregar/cambiar su avatar y también el password.

<br>

![avatar](https://raw.githubusercontent.com/NicolasCaminos/ProyectoFinal-main/main/aplicacion/static/aplicacion/assets/avatar.gif)

<br><br>

6 - En cada una de las secciones que representan Clases se podrá consultar una tabla con los registros cargados en la base de datos y clickeando el botón de que permite agregar un nuevo elemento se abrirá un modal para la carga de todos los datos, de completar todo correctamente se redirigirá a una page de confirmación y se podrá ver la nueva entrada.

<br>

![tercero](https://raw.githubusercontent.com/NicolasCaminos/ProyectoFinal-main/main/aplicacion/static/aplicacion/assets/avatar.gif)

<br><br>

7 - En la última columna de la tabla de cada modelo encontramos "Acciones", donde hay 3 botones que nos permiten ver el detalle, modificar el elemento y eliminarlo.

<br>

![cuarto](https://raw.githubusercontent.com/NicolasCaminos/ProyectoFinal-main/main/aplicacion/static/aplicacion/assets/cuarto.gif)



<br><br>

8 - Existe un superuser con user "admin" y pass "admin" que al acceder podrá visualizar un panel de administrador en el nav superior (usuarios comunes creados desde el registro web no visualizan esta opción), clickeando allí se redirigirá al panel de Django.

<br>

![quinto](https://raw.githubusercontent.com/NicolasCaminos/ProyectoFinal-main/main/aplicacion/static/aplicacion/assets/quinto.gif)

<br>

