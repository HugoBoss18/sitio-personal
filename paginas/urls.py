# paginas/urls.py
from django.urls import path

from .views import VistaAcercaDe, vista_inicio, VistaProyectos, vista_saludo, vista_cuadrado

urlpatterns = [
    # path("proyectos/", vista_proyectos),
    path("cuadrado/<int:numero>/", vista_cuadrado, name="cuadrado"),
    path("saludo/<str:nombre>/", vista_saludo, name="saludo"),  # nuevo
    path("proyectos/", VistaProyectos.as_view(), name="proyectos"),
    path("acerca-de/", VistaAcercaDe.as_view(), name="acerca_de"),
    path("", vista_inicio, name="inicio"),
    
]