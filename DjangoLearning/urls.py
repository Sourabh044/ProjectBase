from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Project.urls')),
    path('User/', include('django.contrib.auth.urls')),
    path('User/signup/', include('Project.urls')),
    
    
]
