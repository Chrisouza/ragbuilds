from django.urls import path
from builds.views import builds

urlpatterns = [
    path('', builds),
]
