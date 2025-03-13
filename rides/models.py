from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('RIDER', 'Rider'),
        ('DRIVER', 'Driver'),
    )
    role = models.CharField(max_length=6, choices=USER_ROLES, default='RIDER')
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Ride(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rides'
    )
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    start_latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    end_latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    end_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"Ride from {self.start_location} to {self.end_location}"
