from rest_framework import serializers
from itens.models import Itens


class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = "__all__"
