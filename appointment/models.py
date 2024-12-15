from django.db import models
from patient.models import Patient
from doctor_app.models import Doctor, AvailableTime
# Create your models here.
APPOINTMENT_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

APPOINTMENT_TYPE = [
    ('Offline','Offline'),
    ('Online','Online'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(choices=APPOINTMENT_TYPE, max_length=30)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS,max_length=30, default="Pending")
    symptom = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name} {self.patient.user.first_name}"
