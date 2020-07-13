from rest_framework import serializers

from .models import Camera

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'
    def to_representation(self,obj):
        data = super(CameraSerializer, self).to_representation(obj)
        data.pop("Position")
        data["Longitude"] = obj.Position.x
        data["Latitude"] = obj.Position.y
        return data
