from django.db import models

class TravelReason(models.Model):
    travel_reason = models.CharField(max_length=50)