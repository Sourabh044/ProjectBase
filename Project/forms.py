from django import forms
from .models import Patient, Appointment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')
        exclude = ['date_recorded', 'user']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('__all__')
        exclude = ['approved', 'name' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs.get('user')
        if user:
            self.fields['patient'].queryset = user.patient_set.all()
