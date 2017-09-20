# pylint: disable=C0103, C0111, R0901


'''
V1 api urls
'''

from django.conf.urls import url, include
from rest_framework import routers

from v1.views import CardViewSet, ListViewSet

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'lists', ListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
