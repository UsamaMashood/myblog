
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acounts/', include('django.contrib.auth.urls')),
    path('acount/', include('acounts.urls')),
    path('', include('blog.urls')),
]
