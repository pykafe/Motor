from models import Motor
from rest_framework import serializers


class MotorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motor
        fields = ('url', 'model', 'engine_size', 'photo', 'fuel')
