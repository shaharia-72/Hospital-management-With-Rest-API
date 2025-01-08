from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from . import models, serializers
from .generate_pdf import generate_pdf


class AppointmentView(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def create(self, request, *args, **kwargs):
        """Override the create method to generate a PDF when an appointment is booked."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Fetch created appointment
        appointment = serializer.instance

        # Prepare data for the PDF
        pdf_context = {
            "patient_name": f"{appointment.patient.user.first_name} {appointment.patient.user.last_name}",
            "doctor_name": f"{appointment.doctor.user.first_name} {appointment.doctor.user.last_name}",
            "appointment_type": appointment.appointment_types,
            "appointment_status": appointment.appointment_status,
            "appointment_time": appointment.time,
            "symptoms": appointment.symptom,
        }

        # Generate PDF
        pdf_file = generate_pdf("pdf_template.html", pdf_context)

        if pdf_file:
            response = HttpResponse(pdf_file, content_type="application/pdf")
            response["Content-Disposition"] = "attachment; filename=appointment_confirmation.pdf"
            return response

        return Response({"detail": "Failed to generate PDF"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
