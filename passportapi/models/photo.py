from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_resource = models.ForeignKey('PhotoResource', on_delete=models.CASCADE, related_name='photo_resource')
    instance_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')