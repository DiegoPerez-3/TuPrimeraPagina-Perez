# CineBlog - Entrega Final Django

## Descripción general
CineBlog es una aplicación web estilo blog desarrollada como entrega final para el curso de Python/Django de Coderhouse. Permite a los usuarios registrarse, publicar reseñas enriquecidas sobre películas y series, gestionar sus propios perfiles y enviarse mensajes privados.

## Funcionalidades
* Autenticación de usuarios (registro, login, logout, cambio de contraseña).
* Creación y gestión de perfiles de usuario con avatar, biografía y enlaces.
* Sistema CRUD completo (Crear, Leer, Actualizar, Borrar) para publicaciones (Pages) con permisos exclusivos para el autor.
* Listado de publicaciones con buscador por título, subtítulo o categoría.
* Editor de texto enriquecido (CKEditor) e imágenes para los artículos.
* Sistema de mensajería interna entre usuarios registrados.

## Apps del proyecto
* **pages**: Maneja todo lo relacionado al blog, listado, creación y visualización de artículos.
* **accounts**: Gestiona los usuarios, perfiles, registro y autenticación.
* **messenger**: Proporciona el sistema de bandeja de entrada y envío de mensajes privados.

## Modelos principales
* `pages.Page`: Representa un artículo o reseña. Contiene título, subtítulo, texto enriquecido, imagen y vinculación con su autor.
* `accounts.Profile`: Extiende el modelo User de Django con avatar, biografía, fecha de nacimiento y página web.
* `messenger.Message`: Representa un mensaje privado con remitente, destinatario, asunto, cuerpo y estado (leído/no leído).

## Rutas principales
* `/`: Inicio del sitio (Home)
* `/about/`: Acerca de
* `/pages/`: Listado de artículos y buscador
* `/pages/create/`: Crear un nuevo artículo
* `/accounts/signup/`: Registro de usuario
* `/accounts/login/`: Iniciar sesión
* `/accounts/profile/`: Perfil de usuario
* `/messages/`: Bandeja de entrada

## Cómo instalar y ejecutar
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual: `.\venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Mac/Linux).
4. Instalar las dependencias: `pip install -r requirements.txt`
5. Ejecutar migraciones: `python manage.py migrate`
6. Iniciar el servidor: `python manage.py runserver`

## Cómo crear un superusuario
Para poder acceder al panel de administración de Django (`/admin/`), debes crear un superusuario:
```bash
python manage.py createsuperuser
```

## Orden recomendado para probar
1. Ejecutar migraciones.
2. Crear superusuario.
3. Entrar al home (`/`).
4. Entrar a `/about/`.
5. Entrar a `/pages/` y ver “No hay páginas aún”.
6. Registrarse.
7. Iniciar sesión.
8. Crear una page con imagen y contenido enriquecido.
9. Ver listado en `/pages/`.
10. Click en “Leer más”.
11. Editar la page.
12. Borrar la page.
13. Entrar al perfil.
14. Editar perfil y avatar.
15. Cambiar contraseña.
16. Crear segundo usuario.
17. Enviar mensaje entre usuarios.
18. Ver bandeja de entrada.
19. Entrar al admin y ver modelos registrados.

## Usuario de prueba sugerido
* Username: `usuario_prueba`
* Email: `prueba@cineblog.com`
*(No se incluyen contraseñas reales en la documentación)*

## Checklist de requisitos cumplidos
- [x] Aplicación `pages` con modelo `Page` e imágenes/texto enriquecido.
- [x] Herencia de HTML en todos los templates.
- [x] Formularios y clases basadas en vistas (CBV).
- [x] Login, Signup, Logout (App `accounts`).
- [x] Modelo `Profile` (avatar, biografía, link).
- [x] App `messenger` (envío de mensajes y bandeja de entrada).
- [x] Rutas, About y Home.
- [x] Todo el contenido registrado en el Admin.
- [x] `requirements.txt` actualizado y exclusión de BDD/archivos media.

## Autor
**Diego Perez** - Proyecto Final Python/Django.