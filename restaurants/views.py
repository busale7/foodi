from django.shortcuts import render
from django.http import HttpResponse
from .models import Business

# Create your views here.
def drink(request) : 
 	context ={
 		"articles" : Business.objects.all(),

 	}
 	return render(request,"foody.html", context)

def drinkeat(request) : 
 	context ={
 		"subjects" : Business.objects.get(name="JORDAN'S DEN"),


 	}
 	return render(request,"fun.html", context)

def eatdrinking(request,name_id): 
 	context ={
 		"articles" : Business.objects.get(id=name_id),


 	}
 	return render(request,"funrun.html", context)

def eat(request) : 
 	context ={
 		"name" :"Joe's Den ",
 		"Description" : " Only Carnivores !  ",
 		"opening" : " 12 pm " ,
 		"closing" : " 12 am ",
 		"title" : "  HELLOO NUMMIES ",
 		"content" : " HERE WE WILL UPDATE YOUR WITH  our specials",

 	}
 	return render(request,"foods.html", context)

def list(request) : 
	context = {
		"articles" : [

{
 		"name" :"Jordan's Den ",
 		"Description" : " Only Carnivores !  ",
 		"opening" : " 12 pm " ,
 		"closing" : " 12 am ",
 		"title" : "  HELLOO NUMMIES ",
 		"content" : " HERE WE WILL UPDATE YOUR WITH  our specials",

 	},{
 		"name" :"Michaels Den ",
 		"Description" : " EVERYONE is Welcome !  ",
 		"opening" : " 12 pm " ,
 		"closing" : " 12 am ",
 		"title" : "  HELLOO Lovers ",
 		"content" : " SPECIAL ANNOUNCEMENT : Michaels 99th Birthday! IS today",

 	},{
 		"name" :"JUJU's CAKES ",
 		"Description" : " Only VEGANS !  ",
 		"opening" : " 12 pm " ,
 		"closing" : " 12 am ",
 		"title" : "  HELLOO VEgans ",
 		"content" : " VEGANS ALL the WAY ",

 	},{
 		"name" :"BROTHers STeaks ",
 		"Description" : " WE LOVE our Customers !  ",
 		"opening" : " 12 pm " ,
 		"closing" : " 10 pm ",
 		"title" : "  Try our Steaks ",
 		"content" : " FREE DRinks ",

 	},{
 		"name" :"EAGLES NATION ",
 		"Description" : " SUPER BOWL winners  ",
 		"opening" : " 12 pm " ,
 		"closing" : " 12 am ",
 		"title" : "  NO Pats fans please ",
 		"content" : " lets eat and greet",

 	}


		]



	}
	return render(request,"foodz.html", context)