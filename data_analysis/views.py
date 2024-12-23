# في data_analysis/views.py
import csv

import openpyxl
from django.shortcuts import render
from .models import Complaint
from .analytics import analyze_complaints
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
import os
from django.conf import settings
import pandas as pd




def home(request):
    return render(request, 'data_analysis/home.html')  # You can create a simple home.html template

def complaint_list(request):
    try:
        # Assuming the file was uploaded successfully
        filename = 'complaints_F065lhp.csv'  # Use the correct file name
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Log the file path for debugging
        print(f"File path: {file_path}")

        # Read the CSV file
        data = pd.read_csv(file_path)

        # Process the data if necessary
        complaints = Complaint.objects.all()  # Fetch all complaints
        return render(request, 'data_analysis/complaints_list.html', {'complaints': complaints})

    except FileNotFoundError:
        return HttpResponse("File not found.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return HttpResponse(f"File uploaded successfully: {uploaded_file_url}")
    return render(request, 'upload.html')

def serve_media(request, path):
    try:
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    except FileNotFoundError:
        raise Http404("File not found")

def complaints_report(request):
    # Fetch all complaints or filter them as per your requirement
    complaints = Complaint.objects.all()

    # Optionally, you can also calculate totals, averages, or other report data here
    total_complaints = complaints.count()

    return render(request, 'data_analysis/complaints_report.html', {
        'complaints': complaints,
        'total_complaints': total_complaints,
    })

def complaints_report_csv(request):
    # Create the HttpResponse object with content type for CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="complaints_report.csv"'

    # Create the CSV writer object
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['Location', 'Complaint Type', 'Description', 'Created At'])

    # Fetch all complaints
    complaints = Complaint.objects.all()

    # Write each complaint to the CSV
    for complaint in complaints:
        writer.writerow([complaint.location, complaint.complaint_type, complaint.description, complaint.created_at])

    return response


def complaints_report_excel(request):
    # Create a new Excel workbook and sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Complaints Report"

    # Write header row
    sheet.append(['Location', 'Complaint Type', 'Description', 'Created At'])

    # Fetch complaints
    complaints = Complaint.objects.all()

    # Write each complaint to a row in the Excel file
    for complaint in complaints:
        sheet.append([complaint.location, complaint.complaint_type, complaint.description, complaint.created_at])

    # Create the HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="complaints_report.xlsx"'

    # Save the workbook to the response
    wb.save(response)

    return response