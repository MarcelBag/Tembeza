from django.shortcuts import render

# rides/views.py

from rest_framework import generics
from .models import Ride
from .serializers import RideSerializer
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt  # Corrected: Import csrf_exempt to bypass CSRF checks


class RideListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve the list of rides or create a new ride.
    """
    queryset = Ride.objects.all().order_by('-created_at')
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can list/create rides


class RideDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a ride by its ID.
    """
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update/delete rides


@csrf_exempt  # Corrected: Bypass CSRF protection for this endpoint
@api_view(['POST'])  # Corrected: Explicitly handle POST requests
def signup(request):
    """
    API endpoint for user signup.
    """
    # Extracting data from the POST request
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password1')
    password2 = request.data.get('password2')

    # Validate passwords match
    if password != password2:
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if username already exists
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

    # Create new user
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


@csrf_exempt  # Corrected: Bypass CSRF protection for this endpoint
@api_view(['POST'])  # Corrected: Explicitly handle POST requests
def signin(request):
    """
    API endpoint for user signin.
    """
    # Extracting data from the POST request
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    # Check if the user exists and credentials are valid
    if user is not None:
        # Generate JWT tokens for authentication
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    # Return error for invalid credentials
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
