"""View module for handling requests about trip notes"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from passportapi.models import Trip, TripNote


class TripNoteView(ViewSet):
    """Passport Trip Note view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip note

        Returns:
            Response -- JSON serialized trip note
        """
        try:
            trip_note = TripNote.objects.get(pk=pk)
            serializer = TripNoteSerializer(trip_note)
            return Response(serializer.data)
        except TripNote.DoesNotExist as ex:
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all trip notes

        Returns:
            Response -- JSON serialized list of trip notes
        """
        trip_notes = TripNote.objects.all()

        if "trip_id" in request.query_params:
            trip_notes = trip_notes.filter(trip=request.query_params['trip_id'])

        serializer = TripNoteSerializer(trip_notes, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new trip note

        Returns:
            Response -- JSON serialized dictionary representation of the new trip note
        """
        serializer = TripNoteSerializer(data=request.data)
        trip = Trip.objects.get(pk=request.data['trip_id'])
        serializer.is_valid(raise_exception=True)
        serializer.save(trip=trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a trip note

        Returns:
            Response -- JSON serialized dictionary representation of the updated trip note
        """
        trip_note = TripNote.objects.get(pk=pk)
        serializer = TripNoteSerializer(trip_note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy a trip note

        Returns:
            Response: None with 204 status code
        """
        try:
            trip_note = TripNote.objects.get(pk=pk)
            trip_note.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except TripNote.DoesNotExist:
            return Response({'message': 'You sent an invalid trip note id'}, status=status.HTTP_404_NOT_FOUND)

class TripNoteSerializer(serializers.ModelSerializer):
    """JSON serializer for trip notes
    """

    class Meta:
        model = TripNote
        fields = ('id', 'trip', 'trip_note',)
        depth = 1