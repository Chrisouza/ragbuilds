from django.contrib import admin
from itens.models import Itens


class ItensAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idItem', 'pk']


admin.site.register(Itens, ItensAdmin)
