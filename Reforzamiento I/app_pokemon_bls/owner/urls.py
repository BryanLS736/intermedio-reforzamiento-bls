from django.urls import path
from . import views

urlpatterns = [
    path('owner_message/', views.owner_message, name='owner_message'),
    path('owner_pais/', views.owner_pais, name='owner_pais'),
    path('owner_lista/', views.owner_lista, name='owner_lista'),
    path('owner_buscar/', views.owner_buscar, name='owner_buscar'),
    path('owner_eliminar/<int:id_owner>/', views.owner_eliminar, name='owner_eliminar'),
    path('owner_editar/<int:id_owner>/', views.owner_editar, name='owner_editar'),
]
