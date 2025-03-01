from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Ride(models.Model):
    user = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride from {self.start_location} to {self.end_location}"
