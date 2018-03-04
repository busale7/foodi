"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('junks/', views.eat),
    path('nums/', views.list),
    path('foos/', views.drink,name="list_list"),
    path('funny/', views.drinkeat),
    path('nofunny/<int:name_id>/', views.eatdrinking, name="name_list"),
    path('idetail/<int:item_id>/', views.item_detail, name="items_detail"),
    path('create/', views.create, name="business_create"),
    path('update/<int:name_id>/', views.update, name="business_update"),
    path('iupdate/<int:item_id>/', views.items_update, name="item_update"),
    path('delete/<int:name_id>/', views.delete, name='delete'),
    path('idelete/<int:item_id>/', views.delete_item, name='itemdelete'),
    path('',views.drink,name="list_list"),
    path('item/',views.item_list,name="item_item"),
    path('signup/',views.signup, name="signup_list"),
    path('login/',views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('add/<int:name_id>/',views.create_Item, name="add_item"),
    path('like/<int:business_id>',views.like, name="like-button"),
    path('likes/<int:items_id>',views.likes, name="like-button"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

