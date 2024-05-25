from django.db import models


# Create your models here.
class Patient(models.Model):
    GENDER = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER)


class ClinicalData(models.Model):
    COMPONENT_NAMES=[('hw', 'Height / Weight'), ('bp', 'Blood Pressure'), ('hr', 'Heart Rate'), ('tmp', 'Temperature')]
    vitalsName = models.CharField(max_length=20, choices=COMPONENT_NAMES)
    vitalsValue = models.CharField(max_length=20)
    vitalsMeasuredDate = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
