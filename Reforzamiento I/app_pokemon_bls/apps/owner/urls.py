from django.urls import path
from . import views

urlpatterns = [
    path('owner_message/', views.owner_message, name='owner_message'),
    path('owner_pais/', views.owner_pais, name='owner_pais'),
    path('owner_lista/', views.owner_lista, name='owner_lista'),
    path('owner_buscar/', views.owner_buscar, name='owner_buscar'),
    path('owner_eliminar/<int:id_owner>/', views.owner_eliminar, name='owner_eliminar'),
    path('owner_editar/<int:id_owner>/', views.owner_editar, name='owner_editar'),

    # Url para vistas basadas en clase
    path('owner_lista_vbc', views.OwnerListView.as_view(), name='owner_lista_vbc'),
    path('owner_create_vbc', views.OwnerCreateView.as_view(), name='owner_create_vbc'),
    path('owner_update_vbc/<int:pk>', views.OwnerUpdateView.as_view(), name='owner_update_vbc'),
    path('owner_delete_vbc/<int:pk>', views.OwnerDeleteView.as_view(), name='owner_delete_vbc'),

    # Url de django rest framework
    path('owner_lista_drf/', views.owner_api_view, name='owner_lista_drf'),
    path('owner_edit_drf/<int:id_owner>', views.owner_api_edit, name='owner_edit_drf'),
]
