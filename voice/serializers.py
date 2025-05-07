from rest_framework import serializers
from .models import Record, Avatar

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'
