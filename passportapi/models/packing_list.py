from django.db import models

class PackingList(models.Model):
    
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='items_to_pack')
    item = models.CharField(max_length=50)
    packed = models.BooleanField(default=False)