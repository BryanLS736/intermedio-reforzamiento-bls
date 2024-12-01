from django.contrib import admin

from pokemon.models import Pokemones
# Register your models here.

@admin.register(Pokemones)
class PokemonesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'generacion', 'tipo')
    search_fields = ('nombre',)
    fields = ('nombre', 'tipo', 'numero')
