"""
URL configuration for tembeza_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from xml.etree.ElementInclude import include
from django.urls import include


from django.contrib import admin
from django.urls import path


# tembeza_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Home page route (or a default landing page)
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/', include('rides.urls')),
    # Frontend UI pages at the top level
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('signin/', TemplateView.as_view(template_name='signin.html'), name='signin'),
    path('map/', TemplateView.as_view(template_name='map.html'), name='map'),

    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include API endpoints from rides app – they will be available under /api/
    path('api/', include('rides.urls')),
]
