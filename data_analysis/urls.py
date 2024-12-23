# data_analysis/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path('complaints/', views.complaint_list, name='complaint_list'),
                  path('complaints/report/', views.complaints_report, name='complaints_report'),
                  path('complaints/report/csv/', views.complaints_report_csv, name='complaints_report_csv'),
                  path('complaints/report/excel/', views.complaints_report_excel, name='complaints_report_excel'),
    # Add other URLs here as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
