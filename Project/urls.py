from django import views
from django.contrib import admin
from django.urls import URLPattern, path , include
from  . import views
urlpatterns = [
    path('', views.homepage, name='DevClinic'),
    # path('User/', views.homepage),
    path('Appointments/', views.appointments, name= "Appointments"),
    path('Patients/All', views.patients, name= "PatientsAll"),
    path('Patients/', views.viewpatients, name= "Patients"),
    path('Appointment/<str:pk>/', views.appointment),
    path('Delete-Appointment/<str:pk>/', views.DeleteAppointment),
    path('Add-Appointment/', views.addappointment, name="Add Appointment"),
    path('Add-Patient/', views.addpatient, name="Add Patient"),
    path('Update-Patient/<str:pk>', views.updatepatient, name="Update Patient"),
    path('User/signup/', views.signup, name="Sign Up"),

] 