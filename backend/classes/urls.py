from django.urls import path
from classes.views import classes

urlpatterns = [
    path('', classes),
]
