from django.forms import ModelForm
from apps.owner.models import Administrador

class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'edad', 'pais', 'vigencia']
