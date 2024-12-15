from django.shortcuts import render

# Create your views here.

def category_message(request):
    data_context = {
        'nombre_owner': 'Jose Araujo',
        'edad': 17,
        'pais': 'Chile'
    }
    return render(request, 'category/category_message.html', context={'data': data_context})
