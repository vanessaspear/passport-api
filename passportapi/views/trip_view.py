"""View module for handling requests about trips"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from passportapi.models import Trip, Reason, TripReason
from django.contrib.auth.models import User


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

        for reason in reasons_selected:
            new_trip_reason = TripReason()
            new_trip_reason.trip = new_trip #   <--- this is an object instance of a trip
            new_trip_reason.reason = Reason.objects.get(pk = reason)#   <--- this is an object instance of a category
            new_trip_reason.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TripReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = ('id', 'reason')

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
    reasons = TripReasonSerializer(many=True)

    class Meta:
        model = Trip
        fields = ('id', 'name', 'city', 'state_or_country', 'departure_date', 'return_date', 'user', 'reasons')
        depth = 1