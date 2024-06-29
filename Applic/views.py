from django.shortcuts import render

def Home(request):
    return render(request, 'Applic/home.html')
# Create your views here.
