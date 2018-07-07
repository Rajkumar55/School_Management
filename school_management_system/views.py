import json
from django.http.response import Http404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import as_serializer_error
from school_management_system.models import Student
from school_management_system.serializers import StudentSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
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
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
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
        try:
            data = json.loads(request.body)
            serializer = StudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'status': 'success', 'message': 'Saved successfully'}
            status_code = status.HTTP_201_CREATED

        except ValueError as ve:
            response = {'status': 'fail', 'message': str(ve)}
            status_code = status.HTTP_400_BAD_REQUEST

        except ValidationError as vve:
            error = list(as_serializer_error(vve).keys())
            error_message = '{} are invalid'.format(', '.join(error))
            response = {'status': 'fail', 'message': error_message}
            status_code = status.HTTP_400_BAD_REQUEST

        except Exception as e:
            response = {'status': 'fail', 'message': str(e)}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response, status=status_code)

    def update(self, request, *args, **kwargs):
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
        try:
            data = json.loads(request.body)
            instance = self.get_object()
            serializer = StudentSerializer(instance, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'status': 'success', 'message': 'Updated successfully'}
            status_code = status.HTTP_200_OK

        except ValueError as ve:
            response = {'status': 'fail', 'message': str(ve)}
            status_code = status.HTTP_400_BAD_REQUEST

        except ValidationError as vve:
            error = list(as_serializer_error(vve).keys())
            error_message = '{} are invalid'.format(', '.join(error))
            response = {'status': 'fail', 'message': error_message}
            status_code = status.HTTP_400_BAD_REQUEST

        except Http404:
            response = {'status': 'fail', 'message': 'Student ID is invalid'}
            status_code = status.HTTP_404_NOT_FOUND

        except Exception as e:
            response = {'status': 'fail', 'message': str(e)}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response, status=status_code)

    def destroy(self, request, *args, **kwargs):
        """
        Delete student

        # URL
            DELETE - http://localhost:8000/student/1/

        # Sample Response
            {
                "status": "success",
                "message": "Deleted Successfully"
            }
        """
        try:
            super(StudentView, self).destroy(request)
            # instance = self.get_object()
            # self.perform_destroy(instance)
            response = {'status': 'success', 'message': 'Deleted Successfully'}
            status_code = status.HTTP_200_OK

        except Http404:
            response = {'status': 'fail', 'message': 'Student ID not available'}
            status_code = status.HTTP_404_NOT_FOUND

        except Exception as e:
            response = {'status': 'fail', 'message': str(e)}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response, status=status_code)
