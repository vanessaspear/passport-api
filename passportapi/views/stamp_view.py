"""View module for handling requests about stamps"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from passportapi.models import Type


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

class TypeSerializer(serializers.ModelSerializer):
    """JSON serializer for stamp types
    """

    class Meta:
        model = Type
        fields = ('id', 'type', )
