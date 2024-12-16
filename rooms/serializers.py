from rest_framework import serializers
from .models import Room, RoomType
import json

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'floor_number', 'room_status', 'room_type']

class RoomTypeSerializer(serializers.ModelSerializer):
    image_path = serializers.ImageField(required=False)

    class Meta:
        model = RoomType
        fields = ['room_type_name', 'base_price', 'capacity', 'room_size', 'room_description', 'amenities', 'facilities', 'image_path']
