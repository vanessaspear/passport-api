from django.db import models

class ItineraryCategory(models.Model):
    
    itinerary = models.ForeignKey("Itinerary", on_delete=models.CASCADE, related_name='itinerary')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='itinerary_categories')
