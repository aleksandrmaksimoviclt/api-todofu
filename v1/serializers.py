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

    id = serializers.ModelField(model_field=Card()._meta.get_field('id'))

    class Meta:
        model = Card
        fields = ('id', 'due_date', 'is_completed', 'label', 'list', 'title')


class ListSerializer(serializers.ModelSerializer):

    '''
    List serializer
    '''

    id = serializers.ModelField(model_field=List()._meta.get_field('id'))
    cards = CardSerializer(many=True, partial=True)


    class Meta:
        model = List
        fields = ('id', 'name', 'cards')

    # Write a .create() method to accept newly created todos
    # check if no duplicates are created

    # def create(self, instance, validated_data):
    #     todos_data = validated_data.pop('todos')

    #     if todos_data:
    #         for todo_data in todos_data:
    #             todo = Todo.objects.filter(id=todo_data['id'])
    #             if not todo:
    #                 Todo.objects.create(**todo_data)

    #     return instance


    def update(self, instance, validated_data):
        todos_data = validated_data.pop('todos')
        list_data = validated_data

        if todos_data:
            for todo_data in todos_data:

                try:
                    todo = Card.objects.filter(id=todo_data['id'])
                except ObjectDoesNotExist:
                    todo = False

                if todo:
                    todo.update(**todo_data)
                elif not todo:
                    Card.objects.create(list_id=list_data['id'], **todo_data)

        return instance


# class BoardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Board
#         fields = '__all__'


# class LabelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Label
#         fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
