from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'phone_no', 'image']

    @admin.display(description="First Name")
    def get_first_name(self, obj):
        return obj.user.first_name

    @admin.display(description="Last Name")
    def get_last_name(self, obj):
        return obj.user.last_name

admin.site.register(Patient, PatientAdmin)
