"""
URL configuration for coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# from coder.view import (
#     saludo,
#     segunda_vista,
#     saluda_nombre,
#     prueba_template,
#     prueba_contexto,
#     prueba_loader,
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("saludo/", saludo),
    # path("segunda/", segunda_vista),
    # path("saluda/<nombre>", saluda_nombre),
    # path("template/", prueba_template),
    # path("template-contexto/", prueba_contexto),
    # path("template-loader/", prueba_loader),
    # path("cursos/", cursos)
    path("app-coder/", include("AppCoder.urls"))
]
