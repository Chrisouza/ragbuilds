from django.urls import path
from itens.views import itens

urlpatterns = [
    path('', itens),
]
