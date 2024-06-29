from django.shortcuts import render

def Home(request):
    return render(request, 'Applic/index.html')

def Acerca(request):
    return render(request, 'Applic/acerca.html')
    
def Contacto(request):
    return render(request, 'Applic/contacto.html')
