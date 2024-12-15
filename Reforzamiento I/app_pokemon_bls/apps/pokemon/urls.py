from django.urls import path
from . import views

urlpatterns = [
    path('pokemon_message/', views.pokemon_message, name='pokemon_message'),
    path('pokemon_tipo/', views.pokemon_tipo, name='pokemon_tipo'),
]
