from django.db import models

class Reason(models.Model):
    
    reason = models.CharField(max_length=50)