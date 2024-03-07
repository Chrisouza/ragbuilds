from django.db import models


class Classes(models.Model):
    nome = models.CharField(max_length=255, default="", unique=True)

    class Meta:
        db_table = "classes"
        verbose_name = "classe"
        verbose_name_plural = "classes"
        ordering = ['nome']
