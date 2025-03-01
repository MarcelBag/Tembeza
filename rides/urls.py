# rides/urls.py

from django.urls import path
from .views import RideListCreateAPIView, RideDetailAPIView

urlpatterns = [
    path('rides/', RideListCreateAPIView.as_view(), name='ride-list-create'),
    path('rides/<int:pk>/', RideDetailAPIView.as_view(), name='ride-detail'),
]