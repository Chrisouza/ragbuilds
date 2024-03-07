from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from itens.models import Itens
from itens.setializer import ItensSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def itens(request):
    all = Itens.objects.all()
    serializer = ItensSerializer(all, many=True)
    return Response(serializer.data)
