from django.db import models

class TripReason(models.Model):
    
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip')
    travel_reason = models.ForeignKey("TravelReason", on_delete=models.CASCADE, related_name='travel_reason')
    