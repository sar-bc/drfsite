from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework import mixins, viewsets

class WomenViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
