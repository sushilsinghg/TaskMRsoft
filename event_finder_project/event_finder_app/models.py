from django.db import models

# Create your models here.# event_finder_app/models.py

class UserPreferences(models.Model):
    location = models.CharField(max_length=100)
    interests = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.location} - {self.interests}"
