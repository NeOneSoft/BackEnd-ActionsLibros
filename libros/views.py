from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autores.models import Autor
from autores.serializers import AutorSerializer
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer, CreateLibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    """
    Libro endpoint (viewset)
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLibroSerializer
        return LibroSerializer

    @action(detail=True, methods=['GET'])
    def autores(self, request, pk=None):
        libro = self.get_object()
        autores = Autor.objects.filter(libro__id=libro.id)
        serialized = AutorSerializer(autores, many=True)
        if not autores:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene autor'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def editoriales(self, request, pk=None):
        libro = self.get_object()
        editoriales = Editorial.objects.filter(libro__id=libro.id)
        serialized = EditorialSerializer(editoriales, many=True)
        if not editoriales:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene editorial'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

