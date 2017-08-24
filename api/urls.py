"""
api URL Configuration
"""

from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/', include('v1.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
