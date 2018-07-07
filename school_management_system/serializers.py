from rest_framework import serializers
from datetime import datetime
from school_management_system.models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(required=True, max_length=100, allow_null=False, allow_blank=False)
    admission_number = serializers.IntegerField(required=True, allow_null=False)
    address = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    school = serializers.CharField(required=True, allow_null=False)
    class_number = serializers.IntegerField(required=True, allow_null=False)
    date_of_joining = serializers.DateField(default=datetime.now().date())
    emergency_contact_number = serializers.CharField(max_length=20, allow_null=True, allow_blank=True)

    class Meta:
        model = Student
        fields = ('student_name', 'admission_number', 'address', 'school', 'class_number', 'date_of_joining',
                  'emergency_contact_number')

    def create(self, validated_data):
        try:
            # Get school instance from the school name
            validated_data['school'] = School.objects.get(name=validated_data['school'])
            student = Student(**validated_data)
            student.save()
            return student

        except School.DoesNotExist as se:
            raise ValueError('School Name is invalid')

    def update(self, instance, validated_data):
        try:
            # Get school instance from the school name
            instance.school = School.objects.get(name=validated_data['school'])

            instance.student_name = validated_data.get('student_name')
            instance.admission_number = validated_data.get('admission_number')
            instance.address = validated_data.get('address')
            instance.class_number = validated_data.get('class_number')
            instance.date_of_joining = validated_data.get('date_of_joining')
            instance.emergency_contact_number = validated_data.get('emergency_contact_number')
            instance.save()
            return instance

        except School.DoesNotExist as se:
            raise ValueError('School Name is invalid')
