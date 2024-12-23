# في data_analysis/models.py

from django.db import models

class Complaint(models.Model):
    location = models.CharField(max_length=255)
    complaint_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds the date when the complaint is created
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')],
        default='Pending'  # Default value is 'Pending'
    )

    def __str__(self):
        return self.description

class CollectionSchedule(models.Model):
    vehicle_id = models.CharField(max_length=50)
    route = models.CharField(max_length=255)
    collection_time = models.DateTimeField()

class Worker(models.Model):
    name = models.CharField(max_length=255)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    assigned_route = models.ForeignKey(CollectionSchedule, on_delete=models.CASCADE)

class DataAnalysis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name