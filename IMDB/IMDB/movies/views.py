from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Movies
from serializers import MoviesSerializer,GenreSerializer
import pdb
@api_view(['GET','POST','PUT'])
def movies_list(request):
	if request.method == 'POST':
		serializer = MoviesSerializer(data = request.data, partial=True)
		if serializer.is_valid():
			#pdb.set_trace()
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'PUT':
		serializer = MoviesSerializer(Movies.objects.get(id=request.data['id']),data = request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#elif request.method == 'DELETE':
    #	Movies.objects.all().delete()
	elif request.method == 'GET':
		movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def genre_add(request):
	serializer = GenreSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
