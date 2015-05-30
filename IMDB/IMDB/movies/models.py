from django.db import models

# Create your models here.

class Movies(models.Model):
	name = models.CharField(max_length=200)
	imdb_score = models.DecimalFields(max_digits=3, decimal_places=1)
  	director = models.CharField(max_length = 100)
  	pupularity = models.DecimalFields(max_digits=4, decimal_places=1)
  	genere = models.ManytoManyField(Genere, related_name="genere")

  	class meta:
  		ordering('name')

class Genere(models.Model):
	genere = models.ManyToManyField(Movies, related_name="genere")