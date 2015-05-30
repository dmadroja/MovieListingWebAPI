from django.forms import widgets
from rest_framework import serializers
from movies.models import Movies,Genere

class MoviesSerializer(serializers.ModelSerializer):
	class meta:
		model = Movies
		fields = ('id','name','imdb_score','directory','popularity','genere')

class GenereSerializer(serializers.Serialize):
 	class meta:
 		model = Genere
 		fields = ('id','genere')