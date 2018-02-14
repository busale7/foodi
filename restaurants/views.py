from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business
from .forms import BusinessesForm

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



def create(request) :
	form = BusinessesForm()
	if request.method == "POST":
			form =BusinessesForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('list_list')
	context ={
		"create_form" : form, 


	}
	return render(request, 'business_create.html', context)


def update(request, name_id):
	business_obj= Business.objects.get(id=name_id)
	form  = BusinessesForm(instance = business_obj)
	if request.method =="POST":
		form =BusinessesForm(request.POST, instance = business_obj)
		if form.is_valid():
			form.save()
			return redirect('list_list')

	context ={
		'business_obj' : business_obj,
		"update_form": form,

	}
	return render(request, 'business_update.html',context)

'''def post_delete(request, name_id):
    instance = Business.objects.get(id=name_id)
    instance.delete()
    return redirect("name_detail")'''
    
def delete(request, name_id) :
	Business.objects.get(id=name_id).delete()
	return redirect("name_detail")
	#name_detail is in the urls.py which will redirect the process to an html file 
