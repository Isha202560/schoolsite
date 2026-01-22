from django import forms
from .models import AdmissionApplication

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ['full_name', 'email', 'phone', 'course', 'message']
