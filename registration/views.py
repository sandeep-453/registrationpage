from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.shortcuts import render
import json
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        registration_data = json.loads(request.body)
        first_name = registration_data.get('firstName')
        last_name = registration_data.get('lastName')
        gender = registration_data.get('gender')
        email = registration_data.get('email')
        mobile_number = registration_data.get('mobileNumber')
        password = registration_data.get('password')

        # Perform necessary validation and registration logic
        # ...

        try:
            # Check for duplicate email or mobile number
            if User.objects.filter(email=email).exists():
                error_message = 'Email already exists. Please use a different email.'
                return JsonResponse({'error': error_message}, status=400)
            if User.objects.filter(mobile_number=mobile_number).exists():
                error_message = 'Mobile number already exists. Please use a different mobile number.'
                return JsonResponse({'error': error_message}, status=400)

            # Save the user details to the database
            user = User(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email=email,
                mobile_number=mobile_number,
                password=password
            )
            user.save()

            # Return a JSON response with a success message
            response_data = {'message': 'Registration successful'}
            return JsonResponse(response_data)
        except IntegrityError:
            error_message = 'Duplicate entry. Registration failed.'
            return JsonResponse({'error': error_message}, status=400)

    # Return an error response for unsupported request methods
    return JsonResponse({'error': 'Invalid request method'}, status=405)
