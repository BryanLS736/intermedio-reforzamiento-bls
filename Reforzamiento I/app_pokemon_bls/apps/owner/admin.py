from django.contrib import admin

from apps.owner.models import Administrador
# Register your models here.

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display=('nombre', 'edad', 'pais', 'vigencia')