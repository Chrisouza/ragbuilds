from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from builds.models import Builds
from builds.setializer import BuildsSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def builds(request):
    all = Builds.objects.all()
    serializer = BuildsSerializer(all, many=True)
    return Response(serializer.data)


def build(request, id):
    pass
