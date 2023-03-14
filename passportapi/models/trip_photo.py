from django.db import models

class TripPhoto(models.Model):
    
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name='trip_photos')