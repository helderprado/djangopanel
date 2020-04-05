from django.contrib import admin
from django.urls import path, include
from panel import views

urlpatterns = [ 
	path('admin/', admin.site.urls), 
	path('', include('panel.urls')),
]