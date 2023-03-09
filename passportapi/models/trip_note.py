from django.db import models

class TripNote(models.Model):
    
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='notes')
    trip_note = models.CharField(max_length=500)
    