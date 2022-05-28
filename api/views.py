from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from paintsite.models import PictureBoard
from .serializers import PictureBoardSerializer, PPDetailSerializer


@api_view(['GET'])
def pps(request):  # Picture posts list (last 10)
    if request.method == 'GET':
        posts = PictureBoard.objects.filter(is_public=True)[:10]
        serializer = PictureBoardSerializer(posts, many=True)
        return Response(serializer.data)


class PPDetailView(RetrieveAPIView):
    queryset = PictureBoard.objects.filter(is_public=True)
    serializer_class = PPDetailSerializer
    # TODO! author__username
