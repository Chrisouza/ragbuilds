from rest_framework import serializers
from builds.models import Builds

from itens.setializer import ItensSerializer
from usuarios.seralizer import UsuariosSerializer
from classes.setializer import ClassesSerializer


class BuildsSerializer(serializers.ModelSerializer):
    classe = ClassesSerializer(read_only=True)
    topo_1 = ItensSerializer(read_only=True)
    topo_2 = ItensSerializer(read_only=True)
    topo_3 = ItensSerializer(read_only=True)

    armadura = ItensSerializer(read_only=True)

    mao_direita = ItensSerializer(read_only=True)
    mao_esquerda = ItensSerializer(read_only=True)
    capa = ItensSerializer(read_only=True)

    sapato = ItensSerializer(read_only=True)

    acessorio_1 = ItensSerializer(read_only=True)
    acessorio_2 = ItensSerializer(read_only=True)
    usuario = UsuariosSerializer(read_only=True)

    class Meta:
        model = Builds
        fields = "__all__"
