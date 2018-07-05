from rest_framework import serializers
from bib.models import ZotItem


class ZotItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZotItem
        fields = "__all__"
