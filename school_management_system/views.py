import json
from rest_framework import viewsets
from rest_framework.response import Response

from school_management_system.models import Student, School
from school_management_system.serializers import StudentSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        """
        List all students

        # URL
            GET - http://localhost/student/

        # Sample Response
            {
                "status": "success",
                "data": [
                    {
                        "student_name": "Ben",
                        "admission_number": 1001,
                        "address": "Coimbatore",
                        "school": "Kongu Vellalar",
                        "class_number": 12,
                        "date_of_joining": "2018-07-06",
                        "emergency_contact_number": null
                    },
                    {
                        "student_name": "Robin",
                        "admission_number": 1002,
                        "address": "Coimbatore",
                        "school": "Kongu Vellalar",
                        "class_number": 12,
                        "date_of_joining": "2018-07-06",
                        "emergency_contact_number": "9944768524"
                    }
                ]
            }
        """
        serializer = StudentSerializer(self.queryset, many=True)
        return Response({'status': 'success', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        """
        Add a new student

        # URL
            POST - http://localhost/student/

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
        try:
            data = json.loads(request.body)
            serializer = StudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'status': 'success', 'message': 'Saved successfully'}

        except School.DoesNotExist as se:
            response = {'status': 'fail', 'message': str(se)}

        except Exception as e:
            response = {'status': 'fail', 'message': str(e)}

        return Response(response)

    def update(self, request, *args, **kwargs):
        """
        Update student details

        # URL
            PUT - http://localhost/student/1/

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
        try:
            data = json.loads(request.body)
            instance = self.get_object()
            serializer = StudentSerializer(instance, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'status': 'success', 'message': 'Updated successfully'}

        except School.DoesNotExist as se:
            response = {'status': 'fail', 'message': str(se)}

        except Exception as e:
            response = {'status': 'fail', 'message': str(e)}

        return Response(response)

    def destroy(self, request, *args, **kwargs):
        """
        Delete student

        # URL
            DELETE - http://localhost/student/1/

        # Sample Response
            {
                "status": "success",
                "message": "Deleted Successfully"
            }
        """
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            response = {'status': 'success', 'message': 'Deleted Successfully'}

        except Exception as e:
            response = {'status': 'fail', 'message': 'Student ID invalid'}

        return Response(response)
