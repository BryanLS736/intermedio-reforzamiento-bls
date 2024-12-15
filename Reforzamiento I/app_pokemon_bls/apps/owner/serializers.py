from rest_framework import serializers
from apps.owner.models import Administrador

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('nombre', 'edad', 'pais', 'vigencia')
