from rest_framework import viewsets, permissions
from .models import Adds
from .serializers import AddSerializers


class AddViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Adds.objects.all().order_by('name')
    serializer_class = AddSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
