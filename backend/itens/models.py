from django.db import models


class Itens(models.Model):
    idItem = models.PositiveIntegerField(default=0, unique=True)
    nome = models.CharField(max_length=255, default="")
    descricao = models.TextField(default="")
    tipo = models.CharField(max_length=255, default="")

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = "itens"
        verbose_name = "item"
        verbose_name_plural = "itens"
        ordering = ["nome"]
