from rest_framework import viewsets
from bib.serializers import ZotItemSerializer
from bib.models import ZotItem


class ZotItemViewSet(viewsets.ModelViewSet):
    queryset = ZotItem.objects.all()
    serializer_class = ZotItemSerializer
