from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),    
    path('pictures/', include ('pictures.urls')),
    path('news/', include ('news.urls'))
    ]