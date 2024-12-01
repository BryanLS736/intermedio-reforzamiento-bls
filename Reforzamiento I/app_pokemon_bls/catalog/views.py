from django.shortcuts import render

# Create your views here.

def catalog_message(request):
    data_context = {
        'nombre_owner': 'Julian Alvarado',
        'edad': 16,
        'pais': 'Argentina'
    }
    return render(request, 'catalog/catalog_message.html', context={'data': data_context})
