from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from classes.models import Classes
from classes.setializer import ClassesSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def classes(request):
    all = Classes.objects.all()
    serializer = ClassesSerializer(all, many=True)
    return Response(serializer.data)
