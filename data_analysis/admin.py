from django.contrib import admin
from .models import Complaint, CollectionSchedule, Worker, DataAnalysis

# Customize admin display for Complaint
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('location', 'complaint_type', 'created_at', 'description')  # Display all fields
    search_fields = ('location', 'complaint_type', 'description')  # Searchable fields
    list_filter = ('created_at', 'complaint_type')  # Filters for admin panel

# Customize admin display for CollectionSchedule
@admin.register(CollectionSchedule)
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'route', 'collection_time')
    search_fields = ('vehicle_id', 'route')
    list_filter = ('collection_time',)

# Customize admin display for Worker
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift_start', 'shift_end', 'assigned_route')
    search_fields = ('name', 'assigned_route__route')  # Search through related fields
    list_filter = ('shift_start', 'shift_end')

# Customize admin display for DataAnalysis
@admin.register(DataAnalysis)
class DataAnalysisAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
