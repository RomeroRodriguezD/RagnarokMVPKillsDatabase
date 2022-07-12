from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login_request, name='index'), #name determina el camino
    path('register', views.register, name="register"), # Registro
    path('registration', views.register), # Registro
    path('database', views.mvp_database, name="database"),
    path("login", views.login_request, name="login1")


    # Ejemplo de pre-defined class con Django
    # path('',TemplateView.as_view(template_name='views/main.html')) -> Entiendo que views puede ser "templates" como carpeta?
    # Otro ejemplos:
    # path('carpeta/<input>', views.nombreview)
    # path ('main', views.MainView.as_view()) -> Revisar as_view().
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Para usar los static
