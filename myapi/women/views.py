from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework import mixins, viewsets


class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     if not pk:
    #         return Women.objects.all()[:3]
    #
    #     return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
