from django.forms import widgets
from rest_framework import serializers
from models import Movies,Genre

class MoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movies
		fields = ('id','name','imdb_score','director','popularity','genre')

class GenreSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Genre
 		fields = ('id','genre')
