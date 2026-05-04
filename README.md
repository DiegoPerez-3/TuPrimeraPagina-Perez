# TuPrimeraPagina+Perez

Proyecto realizado para la tercera entrega del curso de Python.

## Descripción

Esta es una página web desarrollada con Django para cargar y consultar reseñas de películas y series.

El proyecto permite:

- Crear géneros.
- Crear películas o series.
- Crear reseñas.
- Buscar películas o series por título.
- Ver un listado de películas y series cargadas.
- Administrar los datos desde el panel de administración de Django.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS básico

## Patrón utilizado

El proyecto utiliza el patrón MVT de Django:

- **Model**: define la estructura de los datos.
- **View**: contiene la lógica de las páginas.
- **Template**: muestra la información en HTML.

## Modelos creados

En el archivo `resenas/models.py` se crearon 3 modelos:

### 1. Genero

Representa el género de una película o serie.

Campos principales:

- `nombre`
- `descripcion`

### 2. PeliculaSerie

Representa una película o serie cargada en la web.

Campos principales:

- `titulo`
- `tipo`
- `genero`
- `anio`
- `descripcion`
- `fecha_creacion`

### 3. Resena

Representa una reseña realizada sobre una película o serie.

Campos principales:

- `pelicula`
- `autor`
- `comentario`
- `puntaje`
- `fecha`

## Formularios disponibles

En el archivo `resenas/forms.py` se crearon los siguientes formularios:

- `GeneroForm`: permite crear géneros.
- `PeliculaSerieForm`: permite crear películas o series.
- `ResenaForm`: permite crear reseñas.
- `BusquedaForm`: permite buscar películas o series por título.

## Herencia de HTML

El proyecto utiliza herencia de plantillas.

El archivo principal es:

```text
resenas/templates/resenas/base.html
```

Desde ese archivo heredan las demás páginas:

```text
inicio.html
formulario.html
lista_peliculas.html
buscar.html
```

Esto permite reutilizar la estructura general de la página, como el encabezado, el menú de navegación y el pie de página.

## Orden recomendado para probar la página

Para probar correctamente el proyecto, se recomienda seguir este orden:

### 1. Crear un género

Entrar a:

```text
/crear-genero/
```

Ejemplo de datos:

```text
Nombre: Ciencia ficción
Descripción: Películas y series relacionadas con tecnología, futuro o viajes espaciales.
```

### 2. Crear una película o serie

Entrar a:

```text
/crear-pelicula/
```

Ejemplo de datos:

```text
Título: Dark
Tipo: Serie
Género: Ciencia ficción
Año: 2017
Descripción: Serie alemana sobre viajes en el tiempo y misterios familiares.
```

### 3. Crear una reseña

Entrar a:

```text
/crear-resena/
```

Ejemplo de datos:

```text
Película: Dark
Autor: Diego
Comentario: Muy buena serie, con una historia compleja y atrapante.
Puntaje: 9
```

### 4. Buscar una película o serie

Entrar a:

```text
/buscar/
```

Ejemplo de búsqueda:

```text
Dark
```

### 5. Ver el listado completo

Entrar a:

```text
/peliculas/
```

## URLs principales del proyecto

| Funcionalidad | URL |
|---|---|
| Inicio | `/` |
| Listado de películas y series | `/peliculas/` |
| Crear género | `/crear-genero/` |
| Crear película o serie | `/crear-pelicula/` |
| Crear reseña | `/crear-resena/` |
| Buscar película o serie | `/buscar/` |
| Panel de administración | `/admin/` |

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:

```bash
cd TuPrimeraPaginaPerez
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

Si se usa CMD:

```bash
venv\Scripts\activate.bat
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

### 8. Abrir la página

En el navegador, entrar a:

```text
http://127.0.0.1:8000/
```

## Base de datos

El proyecto utiliza SQLite, que es la base de datos por defecto de Django.

Los datos se guardan en el archivo:

```text
db.sqlite3
```

Las tablas principales creadas corresponden a los modelos:

- `Genero`
- `PeliculaSerie`
- `Resena`

## Panel de administración

Para entrar al panel de administración:

```text
http://127.0.0.1:8000/admin/
```

Desde ahí se pueden administrar:

- Géneros
- Películas o series
- Reseñas

## Estructura general del proyecto

```text
TuPrimeraPaginaPerez/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── resenas/
│   ├── migrations/
│   ├── templates/
│   │   └── resenas/
│   │       ├── base.html
│   │       ├── inicio.html
│   │       ├── formulario.html
│   │       ├── lista_peliculas.html
│   │       └── buscar.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3
```

## Autor

Diego Perez