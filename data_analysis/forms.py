# في data_analysis/forms.py

from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['location', 'complaint_type', 'description']
