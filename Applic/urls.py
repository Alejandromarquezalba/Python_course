from django.urls import path, include
from MyProject.views import *
from Applic.views import *

urlpatterns = [
    path('', Home, name='home'),
    path('acerca/', Acerca, name='acerca'),
    path('contacto/', Contacto, name='contacto')

]

