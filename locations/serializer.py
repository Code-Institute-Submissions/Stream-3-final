from rest_framework import serializers
from .models import mapDetails


class mapDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = mapDetails
        fields = ('center1', 'center2', 'name', 'zoom', 'width')

