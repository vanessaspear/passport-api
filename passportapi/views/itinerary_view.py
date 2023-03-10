"""View module for handling requests about itineraries"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from passportapi.models import Itinerary, Category, ItineraryCategory, Trip
from passportapi.views import TripSerializer, UserTripSerializer


class ItineraryView(ViewSet):
    """Passport Itinerary view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single itinerary

        Returns:
            Response -- JSON serialized itinerary
        """
        try:
            itinerary = Itinerary.objects.get(pk=pk)
            serializer = ItinerarySerializer(itinerary)
            return Response(serializer.data)
        except Itinerary.DoesNotExist as ex:
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all itineraries

        Returns:
            Response -- JSON serialized list of itineraries
        """
        itineraries = Itinerary.objects.all()

        if "trip_id" in request.query_params:
            itineraries = itineraries.filter(trip=request.query_params['trip_id'])

        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new itinerary

        Returns:
            Response -- JSON serialized dictionary representation of the new itinerary
        """
        serializer = CreateItinerarySerializer(data=request.data)
        trip = Trip.objects.get(pk=request.data['trip'])
        serializer.is_valid(raise_exception=True)
        new_itinerary = serializer.save(trip=trip)

        # Many to many relationship
        categories_selected = request.data['categories']
        try:
            for category in categories_selected:
                new_itinerary_category = ItineraryCategory()
                new_itinerary_category.itinerary = new_itinerary #   <--- this is an object instance of a itinerary
                new_itinerary_category.category = Category.objects.get(pk = category)#   <--- this is an object instance of a category
                new_itinerary_category.save()
        except Category.DoesNotExist:
            return Response({'message': 'You sent an invalid category'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a itinerary

        Returns:
            Response -- JSON serialized dictionary representation of the updated itinerary
        """
        itinerary = Itinerary.objects.get(pk=pk)
        serializer = CreateItinerarySerializer(itinerary, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Many to many relationship
        categories_selected = request.data['categories']

        # Remove all itinerary category relationships for this itinerary
        current_relationships = ItineraryCategory.objects.filter(itinerary__id=pk)
        current_relationships.delete()

        # Re-define relationships between the itinerary and categories for the itinerary
        try:
            for category in categories_selected:
                new_itinerary_category = ItineraryCategory()
                new_itinerary_category.itinerary = itinerary
                new_itinerary_category.category = Category.objects.get(pk=category)
                new_itinerary_category.save()
        except Category.DoesNotExist:
            return Response({'message': 'You sent an invalid category'}, status=status.HTTP_404_NOT_FOUND)
       
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy an itinerary

        Returns:
            Response: None with 204 status code
        """
        try:
            itinerary = Itinerary.objects.get(pk=pk)
            itinerary.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Itinerary.DoesNotExist:
            return Response({'message': 'You sent an invalid itinerary'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(methods=['get'], detail=False)
    def categories(self, request):
        """
        @api {GET} /itineraries/categories GET available itinerary categories
        """

        if request.method == 'GET':
            categories = Category.objects.all()

            serializer = CategorySerializer(
                categories, many=True, context={'request': request})
            return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', "category")

class CreateItinerarySerializer(serializers.ModelSerializer):
    """JSON serializer for itineraries
    """

    class Meta:
        model = Itinerary
        fields = ('id', 'name', 'itinerary_description', 'date', 'start_time', 'end_time', 'city', 'state_or_country', 'trip')
        depth = 1

class ItinerarySerializer(serializers.ModelSerializer):
    """JSON serializer for itineraries
    """

    class Meta:
        model = Itinerary
        fields = ('id', 'name', 'itinerary_description', 'date', 'start_time', 'end_time', 'city', 'state_or_country', 'trip', 'categories')
        depth = 1
