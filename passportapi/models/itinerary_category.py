from django.db import models

class ItineraryCategory(models.Model):
    itinerary_category = models.CharField(max_length=50)