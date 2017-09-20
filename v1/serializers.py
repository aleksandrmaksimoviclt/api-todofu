# pylint: disable=C0103

'''
API v1 Serializer
'''
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from v1.models import Card, List


class CardSerializer(serializers.ModelSerializer):

    '''
    Card serializer
    '''

    class Meta:
        model = Card
        fields = ('id', 'list', 'title')


class ListSerializer(serializers.ModelSerializer):

    '''
    List serializer
    '''

    cards = CardSerializer(many=True, partial=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'cards')

    def create(self, validated_data):
        list_data = validated_data
        list = List.objects.create(name=list_data['name'])

        return list
