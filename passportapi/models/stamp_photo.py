from django.db import models


class StampPhoto(models.Model):
    image = models.ImageField(upload_to='photos', height_field=None,
        width_field=None, max_length=None, null=True, blank=True)
    description = models.CharField(max_length=500)
    trip = models.ForeignKey("Trip", on_delete=models.DO_NOTHING, related_name='stamp_photo_trip')
    itinerary = models.ForeignKey("Itinerary", null=True, on_delete=models.DO_NOTHING, related_name='stamp_photo_itinerary')
    type = models.ForeignKey("Type", on_delete=models.DO_NOTHING, related_name='stamp_photo_type')
    date_created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ( '-date_created', )
    