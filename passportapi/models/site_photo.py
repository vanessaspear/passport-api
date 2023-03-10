from django.db import models
from django.contrib.auth.models import User

class SitePhoto(models.Model):
    
    image = models.ImageField(upload_to='photos', null=True, blank=True)
