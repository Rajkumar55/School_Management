import json
from rest_framework import status, generics
from rest_framework.response import Response
from school_management_system.models import Student, School
from school_management_system.serializers import StudentSerializer


class StudentView(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        """
        List all students

        # URL
            GET - http://localhost:8000/student/

        # Sample Response
            {
                "status": "success",
                "data": [
                    {
                        "student_name": "Ben",
                        "admission_number": 1001,
                        "address": "Coimbatore",
                        "school_id": 1,
                        "class_number": 12,
                        "date_of_joining": "2018-07-06",
                        "emergency_contact_number": null
                    },
                    {
                        "student_name": "Robin",
                        "admission_number": 1002,
                        "address": "Coimbatore",
                        "school_id": 1,
                        "class_number": 12,
                        "date_of_joining": "2018-07-06",
                        "emergency_contact_number": "9944768524"
                    }
                ]
            }
        """
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Add a new student

        # URL
            POST - http://localhost:8000/student/

        # Sample Request
            {
                "student_name": "Ben",
                "admission_number": 1001,
                "address": "Coimbatore",
                "school": "KVMHSS",
                "class_number": 12,
                "date_of_joining": "2018-07-05",
                "emergency_contact_number": "9944768524"
            }

        # Sample Response
            {
                "status": "success",
                "message": "Saved successfully"
            }
        """
        data = json.loads(request.body)
        school = School.objects.get(name=data.get('school', ''))
        data['school_id'] = school.id
        serializer = StudentSerializer(data=data)
        is_valid = serializer.is_valid()
        if is_valid:
            serializer.save()
            response = {'status': 'success', 'message': 'Saved successfully'}
            status_code = status.HTTP_201_CREATED

        else:
            response = {'status': 'fail', 'message': serializer.errors}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_code)

    def put(self, request, *args, **kwargs):
        """
        Update student details

        # URL
            PUT - http://localhost:8000/student/1/

        # Sample Request
            {
                "student_name": "Ben Tennyson",
                "admission_number": 1001,
                "address": "Coimbatore",
                "school": "KVMHSS",
                "class_number": 12,
                "date_of_joining": "2018-07-05",
                "emergency_contact_number": "9944768524"
            }

        # Sample Response
            {
                "status": "success",
                "message": "Updated successfully"
            }
        """
        data = json.loads(request.body)
        student = self.get_object()

        school = School.objects.get(name=data.get('school', ''))
        data['school_id'] = school.id
        serializer = StudentSerializer(student, data=data)
        is_valid = serializer.is_valid()
        if is_valid:
            serializer.save()
            response = {'status': 'success', 'message': 'Updated successfully'}
            status_code = status.HTTP_200_OK

        else:
            response = {'status': 'fail', 'message': serializer.errors}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_code)

    def delete(self, request, *args, **kwargs):
        """
        Delete student

        # URL
            DELETE - http://localhost:8000/student/1/

        """
        student = self.get_object()
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
