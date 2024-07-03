from django.shortcuts import render
from .forms import *
from .models import *

def Home(request):

    content1 = {'client': Client.objects.all()}
    content2 =  {'market': Market.objects.all()}
    content3 = {'worker': Worker.objects.all()}
    content = {
                'content1':content1,
                'content2':content2,
                'content3':content3
               }
    print(content)
    return render(
        request, 
        'Applic/index.html', content)


#def Home2(request):
#    content2 = {'market': Market.objects.all()}
#    return render(request, 'Applic/index.html', content2)
#def Home3(request):
#    content3 = {'worker': Worker.objects.all()}
#    return render(request, 'Applic/index.html', content3)


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


def Form2 (request):
    if request.method== 'POST':
        form = classForm2(request.POST)
        if form.is_valid():
            data_money = form.cleaned_data.get('money'),
            data_client = form.cleaned_data.get('client')
            form_save = Client(money=data_money, client=data_client)
            form_save.save()
            
            return render(request, 'Applic/Form.html')
    else:
        form = classForm2()
    
    return render(request, 'Applic/Form.html', {'form':form})


def Form3 (request):
    if request.method== 'POST':
        form = classForm3(request.POST)
        if form.is_valid():
            data_pay = form.cleaned_data.get('pay'),
            data_hours = form.cleaned_data.get('hours')
            form_save = Client(pay=data_pay, hours=data_hours)
            form_save.save()
            
            return render(request, 'Applic/Form.html')
    else:
        form = classForm3()
    
    return render(request, 'Applic/Form.html', {'form':form})


def Search (request):
    return render(request, 'Applic/search.html')

def Find(request):
    if request.GET.get('buscar'):
        patron =  request.GET.get('buscar')
        filt = Client.objects.filter(nombre__icointains=patron)
        content = {'client': filt}
    else:
        content = {'client': Client.objects.all()}
    return render(request, 'Applic/index.html', content)

