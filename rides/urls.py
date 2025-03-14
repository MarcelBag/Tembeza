from django.urls import path
from django.views.generic import TemplateView
from .views import RideListCreateAPIView, RideDetailAPIView, signup, signin

urlpatterns = [
    # API endpoints (backend)
    path('api/rides/', RideListCreateAPIView.as_view(), name='ride-list-create'),  # Handles rides API
    path('api/rides/<int:pk>/', RideDetailAPIView.as_view(), name='ride-detail'),  # Handles single ride API

    # Corrected: Explicitly separate API endpoints for signup/signin
    path('api/signup/', signup, name='api-signup'),  # Maps API signup to handle POST
    path('api/signin/', signin, name='api-signin'),  # Maps API signin to handle POST

    # Frontend routes (templates)
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),  # Frontend signup form
    path('signin/', TemplateView.as_view(template_name='signin.html'), name='signin'),  # Frontend signin form
    path('map/', TemplateView.as_view(template_name='map.html'), name='map'),  # Map page
]
