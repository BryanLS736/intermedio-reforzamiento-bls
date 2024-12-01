from django.contrib import admin

from catalog.models import Catalogo
# Register your models here.

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    pass