from django.db import models

class StampJournal(models.Model):
    name = models.CharField(max_length=50)
    entry = models.CharField(max_length=500)
    trip = models.ForeignKey("Trip", on_delete=models.DO_NOTHING, related_name='stamp_journal_trip')
    itinerary = models.ForeignKey("Itinerary", null=True, on_delete=models.DO_NOTHING, related_name='stamp_journal_itinerary')
    type = models.ForeignKey("Type", on_delete=models.DO_NOTHING, related_name='stamp_journal_type')
    date_created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    