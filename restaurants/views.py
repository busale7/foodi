from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business , Items, favorit, favorits
from django.http import JsonResponse ,Http404 , HttpResponse
from .forms import BusinessesForm ,SignupForm, LoginForm, ItemForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def drink(request) : 
	if request.user.is_anonymous:
		returnredirect('list_list')
	object_list = Business.objects.all()
	object_list =object_list.order_by('name', 'add_date')
	query =request.GET.get('q')
	if query:
		object_list=object_list.filter(title_contains=query)

	liked_posts =[]
	likes =request.user.favorit_set.all()
	for like in likes: 
		liked_posts.append(like.restaurant)
	context={
		"articles" : object_list,
		"my_likes": liked_posts,
	}
	return render(request, "foody.html", context)

'''def drink(request) : 
 	context ={
 		"articles" : Business.objects.all(),

 	}
 	return render(request,"foody.html", context)'''

def item_list(request):
	if request.user.is_anonymous:
		returnredirect('item_item')
	object_list = Items.objects.all()
	object_list =object_list.order_by('name', 'add_date')
	query =request.GET.get('q')
	if query:
		object_list=object_list.filter(title_contains=query)

	liked_posts =[]
	likes =request.user.favorits_set.all()
	for like in likes: 
		liked_posts.append(like.item)
	context ={
		"itemss": Items.objects.all(),
		"my_like": liked_posts,
	
	}
	return render(request,"itemslist.html",context)

def drinkeat(request) : 
 	context ={
 		"subjects" : Business.objects.get(id=1),


 	}
 	return render(request,"fun.html", context)

def eatdrinking(request,name_id): 
 	context ={
 		"articles" : Business.objects.get(id=name_id),


 	}
 	return render(request,"funrun.html", context)

def item_detail(request,item_id): 
 	context ={
 		"itemz" : Items.objects.get(id=item_id),


 	}
 	return render(request,"itemsdetail.html", context)

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
	'''if not (request.user.is_staff or request.user.is_superuser):
					raise Http404'''
	form = BusinessesForm(request.POST or None , request.FILES or None)
	if form.is_valid():
		post =form.save(commit= False)
		post.owner=request.user
		post.save()
		messages.success(request,"Successfully Created")
		return redirect('list_list')
	context ={
		"create_form" : form
			
			
				}
	return render(request, 'business_create.html', context)
	

	'''if request.method == "POST":
						form =BusinessesForm(request.POST, request.FILES or None)
						if form.is_valid():
							business_object =form.save(commit=False)
							business_object.restaurant= User.objects.get(id=request.user.id)
							business_object.save()
							return redirect('list_list')
				context ={
					"create_form" : form
			
			
				}
				return render(request, 'business_create.html', context)
			'''

def update(request, name_id):
	business_obj= Business.objects.get(id=name_id)
	form  = BusinessesForm(instance = business_obj)
	if not(request.user.is_staff or request.user==business_obj.owner):
		#raise Http404
		return HttpResponse("<h1> AMIGO YOU CANT ACCESS the page!</h1>")
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

def items_update(request, item_id):
	item_obj= Items.objects.get(id=item_id)
	form  = ItemForm(instance = item_obj)
	if request.method =="POST":
		form =ItemForm(request.POST, instance = item_obj)
		if form.is_valid():
			form.save()
			return redirect('item_item')

	context ={
		'item_obj' : item_obj,
		"item_update_form": form,

	}
	return render(request, 'item_update.html',context)

'''def post_delete(request, name_id):
    instance = Business.objects.get(id=name_id)
    instance.delete()
    return redirect("name_detail")
	i changed name_detail to list_list
    '''
    
def delete(request, name_id) :
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	Business.objects.get(id=name_id).delete()
	return redirect("list_list")
	#name_detail is in the urls.py which will redirect the process to an html file 

def delete_item(request, item_id) :
	Items.objects.get(id=item_id).delete()
	return redirect("item_item")
	#name_detail is in the urls.py which will redirect the process to an html file 

def signup(request):
	form =SignupForm()
	if request.method =="POST":
		form = SignupForm(request.POST)
		if form.is_valid():   #request.method =="POST":
			user =form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect("list_list")
	context ={
		"form":form
	}
	return render(request, 'signup.html', context)

def user_login(request):
	form = LoginForm()
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			authen = authenticate(username=username ,password=password)
			if authen is not None:
				login(request, authen)
				return redirect("list_list")
	context ={
		"form":form
	}
	return render(request, 'login.html', context)


def user_logout(request):
	logout(request)
	return redirect('login')



def create_Item(request ,name_id) :
	business=Business.objects.get(id=name_id)
	form = ItemForm()
	if request.method == "POST":
		form =ItemForm(request.POST)
		if form.is_valid():
			item_obj = form.save(commit=False)
			item_obj.restaurant = business
			item_obj.save()
			return redirect('item_item')
	context ={
		"Item_form" : form,
		"name_id": name_id,


	}
	return render(request, 'create_item.html', context)



def like(request, business_id):
	favorit_obj = Business.objects.get(id=business_id)
	buz_obj, created = favorit.objects.get_or_create(user=request.user, restaurant=favorit_obj)
	if created :
		action="favorit"
	else: 
		action="Not favorit"
		buz_obj.delete()
	
	favorit_count = favorit_obj.favorit_set.all().count()

	#message="HEllo"
	context={
		#"message": message 
		"action":action,
		"count":favorit_count,


	}
	return JsonResponse(context,safe=False)

def likes(request, items_id):
	likes_obj = Items.objects.get(id=items_id)
	buzz_obj, created = favorits.objects.get_or_create(user=request.user, item=likes_obj)
	if created :
		action="favorit"
	else: 
		action="Not favorit"
		buzz_obj.delete()
	
	favorits_count = likes_obj.favorits_set.all().count()

	#message="HEllo"
	context={
		#"message": message 
		"action":action,
		"count":favorits_count,


	}
	return JsonResponse(context,safe=False)

