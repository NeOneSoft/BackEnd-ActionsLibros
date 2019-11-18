from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido', 'correo', 'telefono')
