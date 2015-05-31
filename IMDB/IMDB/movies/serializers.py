from django.forms import widgets
from rest_framework import serializers
from models import Movies,Genre

class MoviesSerializer(serializers.ModelSerializer):
	genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='genre'
     )
	class Meta:
		model = Movies
		fields = ('id','name','imdb_score','director','popularity','genre')

class GenreSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Genre
 		fields = ('id','genre')
