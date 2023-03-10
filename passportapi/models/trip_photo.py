from django.db import models
from django.contrib.auth.models import User

class TripPhoto(models.Model):
    
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name='trip_photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trip_photos_uploaded')