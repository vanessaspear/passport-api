from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_or_country = models.CharField(max_length=50)
    departure_date = models.DateField(auto_now=False, auto_now_add=False)
    return_date = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planned_trips')
