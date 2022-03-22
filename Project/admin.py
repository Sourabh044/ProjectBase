from django.contrib import admin
# Register your models here.
# from .models import Appointment
from . models import PatientVisit, Patient, PatientBill, PatientFeedback
from . models import Appointment, HealthHistory, Prescription

# admin.site.register(Appointment)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "email", "date_recorded")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("Appointment", "prescribed_on", "prescription_notes")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ( "description", "date_requested", "approved")

@admin.register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_date")

@admin.register(PatientBill)
class PatientBillAdmin(admin.ModelAdmin):
    list_display = ("patient", "treatment_date", "amount", "payment_date")

@admin.register(PatientFeedback)
class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ("patient", "comment", "date_commented")

@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "history")

admin.site.site_title = "CLINIC MANAGEMENT SYSTEM"
admin.site.site_header = "CLINIC MANAGEMENT SYSTEM"
