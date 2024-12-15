from django.db import models
from django.contrib.auth.models import User


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
    image = models.ImageField(upload_to="doctor/images/") 
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    availableTime = models.ManyToManyField(AvailableTime)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
