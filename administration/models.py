from django.db import models

# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(max_length=20)
    budget = models.CharField(max_length=10)
    state = models.CharField(max_length=3)
    owner = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    

class Markaz(models.Model):
    institut = models.CharField(max_length=20)
    center_name = models.CharField(max_length=20)
    place = models.CharField(max_length=30)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)


class HealthData(models.Model):
    patient_name = models.CharField(max_length=20)
    medecin = models.CharField(max_length=30)
    constante = models.CharField(max_length=30, null=True, blank=True)
    prescription = models.TextField(max_length=2000, null=True, blank=True)
    diagnostique = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)