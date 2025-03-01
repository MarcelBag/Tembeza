# rides/urls.py

# rides/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import RideListCreateAPIView, RideDetailAPIView #, OSRMRouteView

urlpatterns = [
    # API endpoints
    path('rides/', RideListCreateAPIView.as_view(), name='ride-list-create'),
    path('rides/<int:pk>/', RideDetailAPIView.as_view(), name='ride-detail'),
    #path('get_route/', OSRMRouteView.as_view(), name='get_route'),

    # Frontend routes (e.g., signup) can also be declared here:
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('signin/', TemplateView.as_view(template_name='signin.html'), name='signin'),
    path('map/', TemplateView.as_view(template_name='map.html'), name='map'),
]
