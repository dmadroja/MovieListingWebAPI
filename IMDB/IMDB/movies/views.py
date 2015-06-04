from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Movies, Genre
from serializers import MoviesSerializer,GenreSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

"""
	View for List, search, add, edit and delete movies
"""

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def movies_operations(request, queryPara =None):
	
	if request.method == 'POST' and request.user.is_superuser:
		serializer = MoviesSerializer(data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'PUT' and request.user.is_superuser:
		serializer = MoviesSerializer(Movies.objects.get(id=request.data['id']),data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE' and request.user.is_superuser:
		Movies.objects.get(id=int(queryPara)).delete()
		return Response(status=status.HTTP_200_OK)

	elif request.method == 'GET':
	
		if queryPara is None or queryPara == '':
			movies = Movies.objects.all()

		if queryPara is not None and queryPara != '':
			movies = Movies.objects.filter(name__icontains= queryPara)
		serializer = MoviesSerializer(movies, many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

"""
	View for adding new genre if required and to list all the genre
"""
@api_view(['POST','GET'])
def genre_operations(request):

	if request.method == 'POST':
		serializer = GenreSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'GET':
		genre = Genre.objects.all()
		serializer = GenreSerializer(genre, many=True)
       	return Response(serializer.data,status=status.HTTP_200_OK)

