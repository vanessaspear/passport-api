from django.db import models
from django.contrib.auth.models import User

class ItineraryPhoto(models.Model):
    
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    itinerary = models.ForeignKey('itinerary', on_delete=models.CASCADE, related_name='itinerary_photos')