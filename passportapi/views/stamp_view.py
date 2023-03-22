"""View module for handling requests about stamps"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import uuid
import base64
from django.core.files.base import ContentFile
from passportapi.models import Type, Trip, Itinerary, StampPhoto


class StampView(ViewSet):
    """Passport Stamp view"""

    @action(methods=['get'], detail=False)
    def types(self, request):
        """Gets all the stamp type options
        @api {GET} /stamps/types GET stamp types
        """
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=False)
    def photos(self, request):
        """Post a new stamp photo
        @api {POST} /stamps/photos POST stamp photo
        """
        
        if request.method == "POST":
            stamp_photo = StampPhoto()
            stamp_photo.description = request.data['description']
            stamp_photo.public = request.data['public']
            
            trip = Trip.objects.get(pk=request.data['trip'])
            stamp_photo.trip = trip
            
            stamp_type = Type.objects.get(pk=request.data['type'])
            stamp_photo.type = stamp_type
            
            try:
                itinerary = Itinerary.objects.get(pk=request.data['itinerary'])
            except Itinerary.DoesNotExist:
                itinerary = request.data['itinerary']
            stamp_photo.itinerary = itinerary
            
            img_format, imgstr = request.data["image"].split(';base64,')
            ext = img_format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'stampPhoto-{uuid.uuid4()}.{ext}')
            stamp_photo.image = data
            
            stamp_photo.save()
            serializer = PhotoSerializer(
                stamp_photo, many=False, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
class TypeSerializer(serializers.ModelSerializer):
    """JSON serializer for stamp types
    """

    class Meta:
        model = Type
        fields = ('id', 'type', )

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for stamp photos
    """

    class Meta:
        model = StampPhoto
        fields = ('id', 'image', 'description', 'public', 'trip', 'itinerary', 'type', 'date_created' )
