from rest_framework import serializers
from .import models

class DoctorSpecializationSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Specialization
        fields = '__all__'

class DoctorDesignationSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Designation
        fields = '__all__'

class DoctorAvailableTimeSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.AvailableTime
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(many=False)
    designation  = serializers.StringRelatedField(many=False)
    specialization  = serializers.StringRelatedField(many=True)
    availableTime  = serializers.StringRelatedField(many=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Doctor
        fields = '__all__'
    
    def get_full_name(self, obj):
        if obj.user:
            return f"{obj.user.first_name} {obj.user.last_name}"
        return None

class DoctorReviewSerializer(serializers.ModelSerializer):
    # user  = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Review
        fields = '__all__'