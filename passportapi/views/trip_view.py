"""View module for handling requests about trips"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from passportapi.models import Trip, Reason, TripReason


class TripView(ViewSet):
    """Passport Trip view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip

        Returns:
            Response -- JSON serialized trip
        """
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist as ex:
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all trips

        Returns:
            Response -- JSON serialized list of trips
        """
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new trip

        Returns:
            Response -- JSON serialized dictionary representation of the new trip
        """
        serializer = CreateTripSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=request.auth.user
        new_trip = serializer.save(user=user)

        # Many to many relationship
        reasons_selected = request.data['reasons']
        try:
            for reason in reasons_selected:
                new_trip_reason = TripReason()
                new_trip_reason.trip = new_trip #   <--- this is an object instance of a trip
                new_trip_reason.reason = Reason.objects.get(pk = reason)#   <--- this is an object instance of a category
                new_trip_reason.save()
        except Reason.DoesNotExist:
            return Response({'message': 'You sent an invalid reason'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a trip

        Returns:
            Response -- JSON serialized dictionary representation of the updated trip
        """
        trip = Trip.objects.get(pk=pk)
        serializer = CreateTripSerializer(trip, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Many to many relationship
        reasons_selected = request.data['reasons']

        # Remove all trip reason relationships for this trip
        current_relationships = TripReason.objects.filter(trip__id=pk)
        current_relationships.delete()

        # Define relationships between the trip and reasons for the trip
        try:
            for reason in reasons_selected:
                new_trip_reason = TripReason()
                new_trip_reason.trip = trip
                new_trip_reason.reason = Reason.objects.get(pk=reason)
                new_trip_reason.save()
        except Reason.DoesNotExist:
            return Response({'message': 'You sent an invalid reason'}, status=status.HTTP_404_NOT_FOUND)
       
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy a trip

        Returns:
            Response: None with 204 status code
        """
        try:
            trip = Trip.objects.get(pk=pk)
            trip.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Trip.DoesNotExist:
            return Response({'message': 'You sent an invalid trip'}, status=status.HTTP_404_NOT_FOUND)

class UserTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', "first_name", "last_name")

class CreateTripSerializer(serializers.ModelSerializer):
    """JSON serializer for creating a trip
    """

    class Meta:
        model = Trip
        fields = ('id', 'name', 'city', 'state_or_country', 'departure_date', 'return_date',)
        depth = 1

class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips
    """
    user = UserTripSerializer(many=False)

    class Meta:
        model = Trip
        fields = ('id', 'name', 'city', 'state_or_country', 'departure_date', 'return_date', 'user', 'reasons')
        depth = 1