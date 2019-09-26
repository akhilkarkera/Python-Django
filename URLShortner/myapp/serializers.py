from rest_framework import serializers
from django.contrib.auth.models import models
from myapp.models import ShortModel

class UrlSerializer(serializers.HyperlinkedModelSerializer): # inbuild method hyperlink generate seperate link for every object
    class Meta:
        model = ShortModel
        fields = (
            'short_url',
            'long_url',
            'url',
        )