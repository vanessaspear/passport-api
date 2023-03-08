from django.db import models

class ItineraryPurpose(models.Model):
    itinerary = models.ForeignKey("Itinerary", on_delete=models.CASCADE, related_name='itinerary')
    itinerary_category = models.ForeignKey("ItineraryCategory", on_delete=models.CASCADE, related_name='itinerary_category')
