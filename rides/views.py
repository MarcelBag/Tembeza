from django.shortcuts import render

# rides/views.py

from rest_framework import generics
from .models import Ride
from .serializers import RideSerializer
from rest_framework.permissions import IsAuthenticated

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
