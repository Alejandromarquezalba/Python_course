from django.template import Template, Context
from django.http import HttpResponse

def saludar (request,nombre,apellido):
    saludo = f'Hola {nombre} {apellido}'
    return HttpResponse(saludo)


def plant (request):

    with open('C:/Users/aranias/Desktop/Python_git/git_test/MyProject/MyProject/plantillas/bienvenida.html') as file:
        templateej = Template(file.read())
        contextej = Context()
        vista = templateej.render(contextej)

    return HttpResponse(vista)