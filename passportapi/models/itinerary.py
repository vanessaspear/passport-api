from django.db import models

class Itinerary(models.Model):
    
    name = models.CharField(max_length=50)
    itinerary_description = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=50)
    state_or_country = models.CharField(max_length=50)
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip_itineraries')
    itinerary_purposes = models.ManyToManyField("ItineraryCategory", through="ItineraryPurpose")