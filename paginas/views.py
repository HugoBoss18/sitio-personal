# paginas/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


def vista_inicio(request):
    contexto = {
        "habilidades": ["Python", "Django", "Git"],
        "mensaje": "GRACIAS por VISITAR mi sitio.",
    }
    return render(request, "paginas/inicio.html", contexto)


class VistaAcercaDe(TemplateView):  # nuevo
    template_name = "paginas/acerca_de.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nombre"] = "Ana"
        contexto["edad"] = 20
        return contexto


# def vista_proyectos(request):
#     contexto = {
#         "proyectos": [
#             {"nombre": "Curriculum Vitae", "descripcion": "Pagina que contenga informacion personal y profesional de un individuo."},
#             {"nombre": "Animacion Increibles", "descripcion": "PAgina para demostrar el uso de la liberea tree.js"},
#             {"nombre": "Blog de cafe", "descripcion": "Pagina dedicada a la venta de cafe y sus derivados.  "},
#         ]
#     }
#     return render(request, "paginas/proyectos.html", contexto)

class VistaProyectos(TemplateView):  # nuevo
    template_name = "paginas/proyectos.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["proyectos"] = [
            {"nombre": "Curriculum Vitae", "descripcion": "Pagina que contenga informacion personal y profesional de un individuo."},
            {"nombre": "Animacion Increibles", "descripcion": "PAgina para demostrar el uso de la liberea tree.js"},
            {"nombre": "Blog de cafe", "descripcion": "Pagina dedicada a la venta de cafe y sus derivados.  "},
        ]
        return contexto


# paginas/views.py
def vista_saludo(request, nombre):  # nuevo
    return render(request, "paginas/saludo.html", {"nombre": nombre})

#Pagina para mostrar el cuadrado de un numero
def vista_cuadrado(request, numero):
    cuadrado = numero ** 2
    return render(request, "paginas/cuadrado.html", {"numero": numero, "cuadrado": cuadrado})