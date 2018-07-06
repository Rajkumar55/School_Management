from rest_framework import serializers
from datetime import datetime
from school_management_system.models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(required=True, max_length=100, allow_null=False, allow_blank=False)
    admission_number = serializers.IntegerField(required=True, allow_null=False)
    address = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    # school = serializers.RelatedField(read_only=True)
    school = serializers.CharField(required=True, allow_null=False)
    # school_id = serializers.IntegerField(required=False)
    class_number = serializers.IntegerField(required=True, allow_null=False)
    date_of_joining = serializers.DateField(default=datetime.now().date())
    emergency_contact_number = serializers.CharField(max_length=20, allow_null=True, allow_blank=True)

    class Meta:
        model = Student
        fields = ('student_name', 'admission_number', 'address', 'school', 'class_number', 'date_of_joining',
                  'emergency_contact_number')

    # def validate(self, attrs):
    #     try:
    #         school = School.objects.get(name=attrs['school'])
    #         # self.school_id = school.id
    #         # self.school = school
    #         attrs['school_id'] = school.id
    #         return attrs
    #
    #     except Exception as e:
    #         # response = {'status': 'fail', 'message': str(e)}
    #         # return response
    #         raise ValueError(str(e))

    def create(self, validated_data):
        try:
            validated_data['school'] = School.objects.get(name=validated_data['school'])
            student = Student(**validated_data)
            student.save()
            return student

        except School.DoesNotExist as se:
            raise ValueError('School Name is invalid')

    def update(self, instance, validated_data):
        try:
            instance.school = School.objects.get(name=validated_data['school'])
            instance.student_name = validated_data.get('student_name')
            instance.admission_number = validated_data.get('admission_number')
            instance.address = validated_data.get('address')
            # instance.school_id = validated_data.get('school_id')
            instance.class_number = validated_data.get('class_number')
            instance.date_of_joining = validated_data.get('date_of_joining')
            instance.emergency_contact_number = validated_data.get('emergency_contact_number')
            instance.save()
            return instance

        except School.DoesNotExist as se:
            # return instance
            raise ValueError('School Name is invalid')
