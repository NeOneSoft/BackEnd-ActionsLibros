from rest_framework import serializers

from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer
from libros.models import Libro


class LibroSerializer(serializers.ModelSerializer):
    """
    General purpose Libro serializer
    """
    autores = AutorSerializer(many=True, read_only=True)
    editorial = EditorialSerializer(read_only=True)

    class Meta:
        model = Libro
        fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')


class CreateLibroSerializer(serializers.ModelSerializer):
    """
    General Libro serializer without related fields
    """
    class Meta:
        model = Libro
        fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')



