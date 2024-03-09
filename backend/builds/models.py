from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from classes.models import Classes
from itens.models import Itens


class Builds(models.Model):
    nome = models.CharField(max_length=255, default="")
    classe = models.ForeignKey(Classes, on_delete=models.CASCADE)

    topo_1 = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='topo_1')
    topo_2 = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='topo_2')
    topo_3 = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='topo_3')

    armadura = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='armadura')

    mao_direita = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='mao_direita')
    mao_esquerda = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='mao_esquerda')

    capa = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='capa')

    sapato = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='sapato')

    acessorio_1 = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='acessorio_1')
    acessorio_2 = models.ForeignKey(
        Itens, on_delete=models.CASCADE, related_name='acessorio_2')

    forca = models.PositiveIntegerField(default=1)
    agilidade = models.PositiveIntegerField(default=1)
    vitalidade = models.PositiveIntegerField(default=1)
    inteligencia = models.PositiveIntegerField(default=1)
    destreza = models.PositiveIntegerField(default=1)
    sorte = models.PositiveIntegerField(default=1)

    observacoes = models.TextField(default="", blank=True, null=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    deslikes = models.PositiveIntegerField(default=0)
    gameplay = models.URLField(default="", blank=True, null=True)
    data_criado = models.DateTimeField(auto_now=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        db_table = "builds"
        verbose_name = "build"
        verbose_name_plural = "builds"
