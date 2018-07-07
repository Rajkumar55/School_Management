from django.db import IntegrityError
from rest_framework.views import Response, exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, IntegrityError) and not response:
        response = Response(
            {
                'status': 'fail',
                'message': 'The given data already available'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    elif isinstance(exc, Exception) and not response:
        response = Response(
            {
                'status': 'fail',
                'message': str(exc)
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return response
