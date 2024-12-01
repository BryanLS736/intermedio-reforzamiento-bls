from django.shortcuts import render, redirect

from owner.models import Administrador

from django.db.models import Q

from owner.forms import AdministradorForm

# Create your views here.


def owner_message(request):
    data_context = {
        'nombre_owner': 'Carlos Sanchez',
        'edad': 31,
        'pais': 'Argentina'
    }

    return render(request, 'owner/owner_message.html', context={'data': data_context})


def owner_pais(request):
    data_context = Administrador.objects.filter(pais='Peru')
    return render(request, 'owner/owner_pais.html', context={'data': data_context})


def owner_lista(request):
    data_context = Administrador.objects.all()
    return render(request, 'owner/owner_lista.html', context={'data': data_context})


def owner_buscar(request):
    buscar = request.GET.get('q','')

    resultados = (
        Q(nombre__icontains=buscar) | Q(pais__icontains=buscar)
    )

    data_context = Administrador.objects.filter(resultados)

    owners_peru = 0
    owners_argentina = 0

    for owner in data_context:
        if owner.pais == 'Peru':
            owners_peru += 1
        elif owner.pais == 'Argentina':
            owners_argentina += 1


    return render(request, 'owner/owner_buscar.html',
                  context={
                      'data': data_context,
                      'query': buscar,
                      'owner_peru': owners_peru,
                      'owner_argentina': owners_argentina
                  })


def owner_eliminar(request, id_owner):
    owner = Administrador.objects.get(id=id_owner)
    owner.delete()
    return redirect('owner_lista')


def owner_editar(request, id_owner):
    owner = Administrador.objects.get(id=id_owner)
    form = AdministradorForm(initial={
        'nombre': owner.nombre,
        'edad': owner.edad,
        'pais': owner.pais,
        'vigencia': owner.vigencia
    })

    if request.method == 'POST':
        form = AdministradorForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_lista')

    return render(request, 'owner/owner_editar.html', context={'form': form})
