from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iblog.urls')),
    # path('tinymce/', include('tinymce.urls')),
        
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "BlogBuzz Admin Portal"
admin.site.site_title = "BlogBuzz Admin Portal"
admin.site.index_title = "Welcome to BlogBuzz"
