from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Business(models.Model):
	name = models.CharField(max_length=125)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time =models.TimeField()
	image = models.ImageField(null=True)
	add_date =models.DateField()

	def __str__(self) : # to set the name of the object in django admin
		return self.name

class Items(models.Model):
	item_name = models.CharField(max_length=125)
	descrip = models.TextField()
	restaurant = models.ForeignKey(Business,default=1, on_delete=models.CASCADE)
	price =models.DecimalField(max_digits=10, decimal_places=5)
	

	def __str__(self) : # to set the name of the object in django admin
		return self.item_name

class favorit(models.Model): 
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant =models.ForeignKey(Business,on_delete=models.CASCADE)

class favorits(models.Model): 
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item =models.ForeignKey(Items,on_delete=models.CASCADE)



'''class Article(models.Model):'''
