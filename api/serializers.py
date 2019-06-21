""" This module contains the api serializes """
from rest_framework import serializers
from core.services.classification_request import ClassificationRequestService
from core.models import ClassificationRequest


class ClassificationRequestSerializer(serializers.ModelSerializer):
    """
    Class to get a dict and save it as an the core.models.ClassificationRequest
    """
    class Meta:
        """
        Serializer meta definitions.
        """
        model = ClassificationRequest
        fields = ('text', 'url', 'response')
        read_only_fields = ('response', )
        extra_kwargs = {
            'text': {'write_only': True},
            'url': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Save the data as a ClassificationRequest after evaluate it
        :param validated_data:
        :return: core.models.ClassificationRequest saved instance
        """
        service = ClassificationRequestService()
        return service.create_request(validated_data['text'], validated_data['url'])

