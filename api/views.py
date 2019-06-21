""" This module contains the views of the trainings """
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import ClassificationRequestSerializer


class FakeViewSet(viewsets.ViewSet):
    def create(self, request):
        """
        Method executed in post requests, request a creation from the serializer and returns the response
        :param request:
        :return:
        """
        serializer = ClassificationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        classification_request = serializer.save()
        return Response(classification_request.response)
