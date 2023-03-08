from django.db import models

class PackingList(models.Model):
    item = models.CharField(max_length=50)
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='items_to_pack')