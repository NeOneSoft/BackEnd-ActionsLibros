from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    """
    Editorial endpoint (viewset)
    """
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None):
        editorial = self.get_object()
        libros = Libro.objects.filter(editorial__id=editorial.id)
        serialized = LibroSerializer(libros, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Esta editorial no tiene libros'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

