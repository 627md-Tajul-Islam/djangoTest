from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootstrap/', include('bootstrap.urls',namespace='bootstrap'))
    
]