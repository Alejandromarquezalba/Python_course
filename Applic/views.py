from django.shortcuts import render
from .forms import *
from .models import *

def Home(request):
    return render(request, 'Applic/index.html')

def Acerca(request):
    return render(request, 'Applic/acerca.html')
    
def Contacto(request):
    return render(request, 'Applic/contacto.html')

def Form (request):
    if request.method== 'POST':
        form = classForm(request.POST)
        if form.is_valid():
            data_money = form.cleaned_data.get('money'),
            data_product = form.cleaned_data.get('product')
            form_save = Client(money=data_money, product=data_product)
            form_save.save()
            
            return render(request, 'Applic/Form.html')
    else:
        form = classForm()
    
    return render(request, 'Applic/Form.html', {'form':form})

