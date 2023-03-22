from django.db import models

class StampProduct(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    link = models.URLField()
    trip = models.ForeignKey("Trip", on_delete=models.DO_NOTHING, related_name='stamp_product_trip')
    itinerary = models.ForeignKey("Itinerary", null=True, on_delete=models.DO_NOTHING, related_name='stamp_product_itinerary')
    type = models.ForeignKey("Type", on_delete=models.DO_NOTHING, related_name='stamp_product_type')
    date_created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ( '-date_created', )