'''
API v1 views
'''

# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from v1.models import Card, List
# from api.serializers import BoardSerializer, \
#                             LabelSerializer, \
#                             ListSerializer, \
#                             TodoSerializer, \
#                             UserSerializer
from v1.serializers import ListSerializer, CardSerializer


class CardViewSet(NestedViewSetMixin, viewsets.ModelViewSet): # pylint: disable=too-many-ancestors

    '''
    Card view
    '''

    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ListViewSet(NestedViewSetMixin, viewsets.ModelViewSet): # pylint: disable=too-many-ancestors

    '''
    List view
    '''

    queryset = List.objects.all()
    serializer_class = ListSerializer


# class BoardViewSet(viewsets.ViewSet):
#     serializer_class = BoardSerializer

#     def list(self, request, user_pk=None):
#         queryset = Board.objects.filter(user=user_pk)
#         serializer = BoardSerializer(queryset, many=True)
#         # return Response(serializer.data)

#     def retrieve(self, request, pk=None, client_pk=None):
#         queryset = Board.objects.filter(pk=pk, client=client_pk)
#         board = get_object_or_404(queryset, pk=pk)
#         serializer = BoardSerializer(board)
#         # return Response(serializer.data)


# class LabelViewSet(viewsets.ViewSet):
#     queryset = Label.objects.all()
#     serializer_class = LabelSerializer


# class ListViewSet(viewsets.ViewSet):
#     serializer_class = ListSerializer

#     def list(self, request, user_pk=None, board_pk=None):
#         queryset = List.objects.filter(board__user = user_pk,
#                                         board = board_pk)
#         serializer = ListSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None, user_pk=None, board_pk=None):
#         queryset = List.objects.filter(pk=pk,
#                                         board=board_pk,
#                                         board__user=user_pk)
#         board = get_object_or_404(queryset, pk=pk)
#         serializer = ListSerializer(board)
#         return Response(serializer.data)


# class TodoViewSet(viewsets.ViewSet):
#     serializer_class = TodoSerializer

#     def list(self, request, user_pk=None, board_pk=None, list_pk=None):
#         queryset = List.objects.filter(list__board__user=user_pk,
#                                         list__board=board_pk,
#                                         list=list_pk)
#         serializer = ListSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None, user_pk=None, board_pk=None):
#         queryset = List.objects.filter(pk=pk,
#                                         list__board__user=user_pk,
#                                         list__board=board_pk,
#                                         list=list_pk)
#         list = get_object_or_404(queryset, pk=pk)
#         serializer = TodoSerializer(list)
#         return Response(serializer.data)


# class UserViewSet(viewsets.ViewSet):
#     serializer_class = UserSerializer

#     def list(self, request,):
#         queryset = User.objects.filter()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.filter()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(User)
#         return Response(serializer.data)
