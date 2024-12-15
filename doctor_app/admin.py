from django.contrib import admin
from .models import Doctor, AvailableTime, Designation,Specialization
# Register your models here.


class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


admin.site.register(Doctor)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(AvailableTime)