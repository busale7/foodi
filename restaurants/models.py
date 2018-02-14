from django.db import models


# Create your models here.
class Business(models.Model):
	name = models.CharField(max_length=125)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time =models.TimeField()


	def __str__(self) : # to set the name of the object in django admin
		return self.name

'''class Article(models.Model):'''
