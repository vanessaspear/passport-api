from django.db import models

class TripReason(models.Model):
    
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip')
    reason = models.ForeignKey("Reason", on_delete=models.CASCADE, related_name='trip_reason')
    