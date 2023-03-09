from django.db import models

class Itinerary(models.Model):
    
    name = models.CharField(max_length=50)
    itinerary_description = models.CharField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=50)
    state_or_country = models.CharField(max_length=50)
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip_itineraries')