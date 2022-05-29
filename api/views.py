from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from paintsite.models import PictureBoard, Comment
from .serializers import PictureBoardSerializer, PPDetailSerializer, CommentSerializer


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


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def comments(request, pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    coms = Comment.objects.filter(is_active=True, pp=pk)
    serializer = CommentSerializer(coms, many=True)
    return Response(serializer.data)

