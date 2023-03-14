"""View module for handling requests about trip photos"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from passportapi.models import Trip, TripPhoto


class TripPhotoView(ViewSet):
    """Passport Trip Photo view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip photo

        Returns:
            Response -- JSON serialized trip photo
        """
        try:
            trip_photo = TripPhoto.objects.get(pk=pk)
            serializer = TripPhotoSerializer(trip_photo)
            return Response(serializer.data)
        except TripPhoto.DoesNotExist as ex:
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all photos

        Returns:
            Response -- JSON serialized list of photos
        """
        trip_photos = TripPhoto.objects.all()

        if "trip_id" in request.query_params:
            trip_photos = trip_photos.filter(trip=request.query_params['trip_id'])

        serializer = TripPhotoSerializer(trip_photos, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new trip photo

        Returns:
            Response -- JSON serialized dictionary representation of the new trip photo
        """
        serializer = TripPhotoSerializer(data=request.data)
        trip = Trip.objects.get(pk=request.data['trip_id'])
        serializer.is_valid(raise_exception=True)
        serializer.save(trip=trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a trip photo

        Returns:
            Response -- JSON serialized dictionary representation of the updated trip photo
        """
        trip_photo = TripPhoto.objects.get(pk=pk)
        serializer = TripPhotoSerializer(trip_photo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy a trip photo

        Returns:
            Response: None with 204 status code
        """
        try:
            trip_photo = TripPhoto.objects.get(pk=pk)
            trip_photo.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except TripPhoto.DoesNotExist:
            return Response({'message': 'You sent an invalid trip photo id'}, status=status.HTTP_404_NOT_FOUND)

class TripPhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for trip photos
    """

    class Meta:
        model = TripPhoto
        fields = ('id', 'trip', 'image',)
        depth = 1