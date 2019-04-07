from django.shortcuts import render
from django.views.generic import CreateView, View, ListView
from .models import Turismo
from .forms import TurismoForm
import requests


def home(request):
    response = requests.get('https://apipontosturisticos.herokuapp.com/pontoturisticos/?format=json')
    list_pontos = response.json()
    print(list_pontos)
    params = {
        'pontos_turisticos': list_pontos,
    }

    return render(request, 'turismo/home.html', params)

        

        
       
    

    
