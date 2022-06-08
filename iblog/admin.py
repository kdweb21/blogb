from calendar import c
from unicodedata import category
from django.contrib import admin
from iblog.models import Category, Post, Contact
 
#for configuration of category in admin
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_id', 'category_icon', 'category_title', 'url',  'add_date', )
    search_fields=('category_title',)
    list_filter=('add_date',)
    # list_per_page=2
    
#for configuration of post in admin
class PostAdmin(admin.ModelAdmin):
    list_display=('post_id', 'post_icon', 'post_title', 'category_id', 'category',  'url',  )
    search_fields=('post_title',)
    list_filter=('category',)
    # list_per_page=3

    class Media:
        js=('https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.10.4/tinymce.min.js','js/script.js', )

class ContactAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email', 'message' )
    search_fields=('first_name',)
    
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
