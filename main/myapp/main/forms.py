from django import forms
from .models import patientregistration

class PatientCreate(forms.ModelForm):
    class Meta:
        model = patientregistration
        fields = '__all__'
        widgets = {
            'fields': forms.TextInput(attrs={'class': 'form-control',  'style': 'width: 300px;'}),
        }
        