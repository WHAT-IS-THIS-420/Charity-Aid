from django import forms
from .models import Recipiant, Appointment

class RecipiantForm(forms.ModelForm):
    class Meta:
        model = Recipiant
        fields = ['fname', 'lname', 'telephone']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'text', 'id': 'id_date'}),
            'time': forms.TimeInput(attrs={'type': 'text', 'id': 'id_time'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }  