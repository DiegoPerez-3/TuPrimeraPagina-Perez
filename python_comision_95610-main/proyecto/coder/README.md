1. Creamos un entorno virtual

python -m venv .venv

2. Activamos el entorno virtual

source .venv/bin/activate

3. Instalamos las dependencias

pip install django

pip install -r requeriments.txt

requeriments.txt -----> pip freeze >> requeriments.txt

4. creamos un proyecto

django-admin startproject <nombre_del_proyecto> .

5. levantamos el servidor de desarrollo

python manage.py runserver

6. Creamos un archivo para las vistas

view.py ---> funciones con las vistas

def saludo(request):
return HttpResponse("Hola mundo!!!")

7. Agregamos la vista en el archivo de urls (urls.py)

   path("saludo/", saludo),

cliente hace get http://localhost:8000/saludo/ --------> servidor desarrollo -----> saludo/ lo busca en el archivo urls --->

---> vista saludo ----> server responde al cliente HTML "Hola mundo!!!.

8. Creamos una carpeta templates

templates ----> archivos html

cliente hace get http://localhost:8000/template/ --------> servidor desarrollo -----> template/ lo busca en el archivo urls ---> prueba_template

---> vista saludo ----> server responde al cliente HTML "Hola mundo!!!.
