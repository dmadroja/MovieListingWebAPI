from rest_framework import serializers
import django.db.models.fields
from models import Movies,Genre
import pdb
class MoviesSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=200, min_length=1, allow_blank=False, trim_whitespace=False, 
			error_messages={"blank": "Movie name cannot be empty."})

	director = serializers.CharField(max_length=100, min_length=1, allow_blank=False, trim_whitespace=False, 
			error_messages={"blank": "director name cannot be empty."})

	genre = serializers.SlugRelatedField(many=True,queryset = Genre.objects.all(),
		slug_field='genre',required = True,error_messages={"blank": "genre cannot be empty."})

	popularity = serializers.FloatField(max_value=100.0, min_value =0.0,error_messages={
            "min_value": "99popularity value should be greater than 0.0",
            "max_value": "99popularity value should be less than 100.0" })

	imdb_score =   serializers.FloatField(max_value=10.0, min_value =0.0,error_messages={
            "min_value": "imdb_score value should be greater than 0.0",
            "max_value": "imdb_score value should be less than 10.0"})

	
	
	class Meta:
		model = Movies
		fields = ('id','name','imdb_score','director','popularity','genre')
	
	"""
		Override the basic methods of serialize and deserialize for making alias for "99popularity"
	"""
	def to_representation(self, obj):
		serialized_data = super(MoviesSerializer, self).to_representation(obj)
		if serialized_data["popularity"] is not None:
			serialized_data["99popularity"] = serialized_data["popularity"]
		else:
			serialized_data["99popularity"] = ''
		del serialized_data["popularity"]
		return serialized_data	

	def to_internal_value(self, data):

		if "99popularity" in data:
			data["popularity"] = data["99popularity"]
		else:
			data["popularity"] = 0.0
		if not "imdb_score" in data:
			data["imdb_score"] = 0.0

		serialized_data = super(MoviesSerializer, self).to_internal_value(data)
		return serialized_data


class GenreSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Genre
 		fields = ('id','genre')

		