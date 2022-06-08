from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.Home),
    path('about/', views.About_Us),
    path('contact/', views.Contact_Us),
    path('category/', views.Cat),
    path('category/<slug:cat>', views.single_category),
    path('blog/<slug:url>', views.Blog_post),
]
