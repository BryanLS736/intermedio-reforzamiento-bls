from django.forms import ModelForm
from owner.models import Administrador

class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'edad', 'pais', 'vigencia']
