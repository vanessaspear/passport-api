"""View module for handling requests about trip notes"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from passportapi.models import Trip, PackingList


class PackingListView(ViewSet):
    """Passport Packing List view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single packing item

        Returns:
            Response -- JSON serialized packing item
        """
        try:
            item = PackingList.objects.get(pk=pk)
            serializer = PackingListSerializer(item)
            return Response(serializer.data)
        except PackingList.DoesNotExist as ex:
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all packing list items

        Returns:
            Response -- JSON serialized list of packing list items
        """
        packing_list = PackingList.objects.all()

        if "trip_id" in request.query_params:
            packing_list = packing_list.filter(trip=request.query_params['trip_id'])

        serializer = PackingListSerializer(packing_list, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new packing item

        Returns:
            Response -- JSON serialized dictionary representation of the new packing item
        """
        serializer = PackingListSerializer(data=request.data)
        trip = Trip.objects.get(pk=request.data['trip_id'])
        serializer.is_valid(raise_exception=True)
        serializer.save(trip=trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a packing item

        Returns:
            Response -- JSON serialized dictionary representation of the updated item
        """
        item = PackingList.objects.get(pk=pk)
        serializer = PackingListSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy a packing item

        Returns:
            Response: None with 204 status code
        """
        try:
            item = PackingList.objects.get(pk=pk)
            item.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PackingList.DoesNotExist:
            return Response({'message': 'You sent an invalid item id'}, status=status.HTTP_404_NOT_FOUND)

class PackingListSerializer(serializers.ModelSerializer):
    """JSON serializer for a packing list
    """

    class Meta:
        model = PackingList
        fields = ('id', 'trip', 'item',)
        depth = 1