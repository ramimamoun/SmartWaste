# waste_management/urls.py

from django.contrib import admin
from django.urls import path, include
from data_analysis import views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data-analysis/', include('data_analysis.urls')),  # Your app's URLs
    path('', views.home, name='home'),  # Add this line to define the root URL
]
