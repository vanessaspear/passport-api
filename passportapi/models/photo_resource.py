from django.db import models

class PhotoResource(models.Model):
    photo_resource = models.CharField(max_length=50)