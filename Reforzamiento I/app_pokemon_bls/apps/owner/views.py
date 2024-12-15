from django.shortcuts import render, redirect
from apps.owner.models import Administrador
from django.db.models import Q
from apps.owner.forms import AdministradorForm

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from rest_framework.decorators import api_view, permission_classes
from apps.owner.serializers import AdministradorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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


# Reforzamiento 3: Vistas basadas en clase

class OwnerListView(ListView):
    model = Administrador
    template_name = 'owner/owner_lista_vbc.html'


class OwnerCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'owner/owner_create_vbc.html'
    success_url = reverse_lazy('owner_lista_vbc')


class OwnerUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'owner/owner_update_vbc.html'
    success_url = reverse_lazy('owner_lista_vbc')

class OwnerDeleteView(DeleteView):
    model = Administrador
    template_name = 'owner/onwer_delete_confirm.html'
    success_url = reverse_lazy('owner_lista_vbc')


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def owner_api_view(request):
    if request.method == 'GET':
         query = Administrador.objects.all()
         serializers_class = AdministradorSerializer(query, many=True)
         return Response(serializers_class.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializers_class = AdministradorSerializer(data=request.data)

        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def owner_api_edit(request, id_owner):
    owner = Administrador.objects.get(id=id_owner)

    if request.method == 'GET':
        serializers_class = AdministradorSerializer(owner)
        return Response(serializers_class.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializers_class = AdministradorSerializer(owner, data=request.data)

        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        owner.delete()
        return Response(f'Owner {owner.nombre} eliminado.', status=status.HTTP_202_ACCEPTED)
