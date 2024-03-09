from django.db import models


class Classes(models.Model):
    idClasse = models.PositiveIntegerField(default=0)
    nome = models.CharField(max_length=255, default="", unique=True)
    img_path = models.CharField(max_length=255, default="")

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = "classes"
        verbose_name = "classe"
        verbose_name_plural = "classes"
        ordering = ['nome']
