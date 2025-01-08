from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="patient/images/", blank=True, null=True)
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Patient)
def delete_user_on_patient_delete(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()
