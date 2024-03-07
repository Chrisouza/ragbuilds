from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from classes.models import Classes
from classes.setializer import ClassesSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def classes(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            body = request.data
            serializer = ClassesSerializer(data=body)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': serializer.errors['nome']}, status=status.HTTP_409_CONFLICT)
    all = Classes.objects.all()
    serializer = ClassesSerializer(all, many=True)
    return Response(serializer.data)
