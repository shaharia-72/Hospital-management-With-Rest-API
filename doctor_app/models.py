from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

class Specialization(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name


class AvailableTime(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctor_app/images/") 
    descriptions = models.TextField(null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    availableTime = models.ManyToManyField(AvailableTime)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    meet_link = models.CharField(max_length=100)
    clinic_address = models.CharField(max_length=255, blank=True, null=True)  # New field
    contact_info = models.CharField(max_length=50, blank=True, null=True)  # New field
    bio = models.TextField(blank=True, null=True)  # New field

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Review by {self.reviewer.user.first_name} for Dr. {self.doctor.user.first_name}"

