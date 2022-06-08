from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Contact

# Create your views here.
def Home(request):
    # cats=Category.objects.all()[:10]
    cats=Category.objects.all()
    posts=Post.objects.all()    
    return render(request, 'index.html', {'cats':cats, 'posts':posts} )  

def About_Us(request):
    cats=Category.objects.all()
    return render(request, 'about.html', {'cats':cats,})  

def Contact_Us(request):
    if  request.method=="POST":

        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        useremail=request.POST.get('email')  
        usermessage=request.POST.get('message')  
    
        a=Contact(first_name=firstname, last_name=lastname, email=useremail, message=usermessage ) 
        a.save()

        data={
            'message':"your query is resived ! thank you for contact:)"
        }

    cats=Category.objects.all()
    return render(request, 'contact.html', {'cats':cats,})  

def Blog_post(request, url):
    singlepost=Post.objects.filter(url=url)
    # singlepost=Post.objects.get(url=url)
    cats=Category.objects.all()
    return render(request, 'post.html', {'single': singlepost, 'cats':cats,})  

def single_category(request, cat):
    singlepost=Post.objects.filter(url=cat)    
    cats=Category.objects.all()
    return render(request, 'singlecat.html', { 'cats':cats, 'singlepost':singlepost})      

def Cat(request,):    
    cat=Category.objects.all()    
    return render(request, 'category.html', {'cat':cat})  
