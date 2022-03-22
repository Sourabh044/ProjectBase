from unicodedata import name
from django.conf import settings
from django.utils import timezone
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


Dr_List = (
    ("Dr. LIM", "Dr. LIM"),
    ("Dr. Meledez", "Dr. Meledez"),
)

class Patient(models.Model):
    # settings.AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    name = models.CharField(max_length=200,null=False, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,null=False, blank=False)
    phone = models.CharField(max_length=200,null=False, blank=False)
    email = models.EmailField(max_length=200,null=False, blank=False)
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Appointment(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    id_number = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True , editable=False)
    description = models.TextField(null=False,blank=False)
    date_requested = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    Dr_Name = models.CharField(max_length=200, choices=Dr_List , default=" ", blank=False)
    created = models.DateTimeField(auto_now_add=True)
  # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name

class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

class Prescription(models.Model):
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    prescribed_on = models.DateTimeField(default=timezone.now)
    prescription_notes = models.TextField()

    def __str__(self):
        return self.Appointment.name

class PatientBill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    payment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.patient.name

class PatientFeedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name
    
class HealthHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    history = models.TextField()

    def __str__(self):
        return self.patient.name

