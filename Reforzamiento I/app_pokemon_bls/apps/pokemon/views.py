from django.shortcuts import render
from apps.pokemon.models import Pokemones
# Create your views here.

def pokemon_message(request):
    data_context = {
        'nombre_owner': 'Luis Pardo',
        'edad': 24,
        'pais': 'Perú'
    }

    return render(request, 'pokemon/pokemon_message.html', context={'data': data_context})

def pokemon_tipo(request):
    data_context = Pokemones.objects.filter(tipo__contains='Fuego')
    return render(request, 'pokemon/pokemon_tipo.html', context={'data': data_context})

