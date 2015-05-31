from django.db import models

# Create your models here.
class Genre(models.Model):
	genre = models.CharField(max_length=50)

class Movies(models.Model):
	name = models.CharField(max_length=200)
	imdb_score = models.FloatField()
  	director = models.CharField(max_length = 100)
  	popularity = models.FloatField()
  	genre = models.ManyToManyField(Genre)

  	class meta:
  		ordering = ['name']
