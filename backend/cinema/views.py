from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import FilmCateg, Film
from .serializers import FilmCategSerializer, FilmSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def ApiOverview(request):
    api_urls = {
        'Film': '/Film/',
        'FilmCateg': '/Categ/',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_film(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = Film.objects.filter(**request.query_params.dict())
    else:
        items = Film.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = FilmSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_filmcateg(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = FilmCateg.objects.filter(**request.query_params.dict())
    else:
        items = FilmCateg.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = FilmCategSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)