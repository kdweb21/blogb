from operator import mod
from unicodedata import name
from django.db import models
from django.forms import CharField
from sklearn.feature_extraction import image
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.
# model category
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_title=models.CharField(max_length=50)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/category')
    add_date=models.DateTimeField(auto_now_add=True, null=True)

    # this method can use as the attribute of the admin to list_display 
    def category_icon(self):
        return format_html('<img src="/media/{}" style="width:50px; height:50px; border-radius:50%" />'.format(self.image))

    def __str__(self) :
        return self.category_title

# model post
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    post_title=models.CharField(max_length=200)
    # content=HTMLField()
    content=models.TextField()
    url=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/post')   

    def post_icon(self):
        return format_html('<img src="/media/{}" style="width:50px; height:50px; border-radius:50%" />'.format(self.image))

    def __str__(self) :
        return self.post_title

# model contact
class Contact(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name + " " + last_name
    