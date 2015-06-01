from django.forms import widgets
from rest_framework import serializers
from models import Movies,Genre
import pdb

class MoviesSerializer(serializers.ModelSerializer):
	genre = serializers.SlugRelatedField(
        many=True,
        queryset = Genre.objects.all(),
        slug_field='genre'
     )
	class Meta:
		model = Movies
		fields = ('id','name','imdb_score','director','popularity','genre')
	
	"""
		Override the basic methods of serialize and deserialize for making alias for "99popularity"
	"""
	def to_representation(self, obj):
		serialized_data = super(MoviesSerializer, self).to_representation(obj)
		serialized_data["99popularity"] = serialized_data["popularity"]
		del serialized_data["popularity"]
		return serialized_data	

	def to_internal_value(self, data):
		data["popularity"] = data["99popularity"]
		serialized_data = super(MoviesSerializer, self).to_internal_value(data)
		return serialized_data

	
	
	

class GenreSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Genre
 		fields = ('id','genre')

		