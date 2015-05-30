from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import Movies
from movies.serializers import MoviesSerializer

@api_view([GET],[POST])
def movies_list(request):
	if request.method == 'POST' && request.META[HTTP_AUTHORIZATION] == '':
		serializer = MoviesSerializer(data = request.data)
		if serializer.isValid:
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'GET':
		movies = Movies.objects.all()
        serializer = MoviesSerializer(snippets, many=True)
        return Response(serializer.data)


#@api_view([GET])
#def movies_search_list(request):
