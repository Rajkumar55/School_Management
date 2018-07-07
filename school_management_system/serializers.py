from rest_framework import serializers
from datetime import datetime
from school_management_system.models import Student


class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(required=True, max_length=100, allow_null=False, allow_blank=False)
    admission_number = serializers.IntegerField(required=True, allow_null=False)
    address = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    school_id = serializers.IntegerField(allow_null=False)
    class_number = serializers.IntegerField(required=True, allow_null=False)
    date_of_joining = serializers.DateField(default=datetime.now().date())
    emergency_contact_number = serializers.CharField(max_length=20, allow_null=True, allow_blank=True)

    class Meta:
        model = Student
        fields = ('student_name', 'admission_number', 'address', 'school_id', 'class_number', 'date_of_joining',
                  'emergency_contact_number')
