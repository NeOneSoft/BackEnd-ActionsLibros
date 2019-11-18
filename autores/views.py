from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autores.models import Autor
from autores.serializers import AutorSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer


class AutorViewSet(viewsets.ModelViewSet):
    """
    Autor endpoint (ViewSet)
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None):
        autor = self.get_object()
        libros = Libro.objects.filter(autores__id=autor.id)
        serialized = LibroSerializer(libros, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este autor no tiene libros'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

