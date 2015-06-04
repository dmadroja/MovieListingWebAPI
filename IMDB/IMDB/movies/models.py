from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
	genre = models.CharField(max_length=50, unique= True)

class Movies(models.Model):
	name = models.CharField(max_length=200)
	imdb_score = models.FloatField()
  	director = models.CharField(max_length = 100)
  	popularity =models.FloatField()
  	genre = models.ManyToManyField(Genre)

  	class Meta:
  		unique_together =  (('name', 'director'),)
