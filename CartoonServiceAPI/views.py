from rest_framework import viewsets,mixins
from .serializers import CameraSerializer
from .models import Camera
from django.contrib.gis.geos import Point
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Retrieve all the cameras from the database."
))
class CameraListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list,many=True)
        return Response({'cameralist':serializer.data})


CenterLatitude = openapi.Parameter('centerlatitude', openapi.IN_QUERY, description="Center Latitude", type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT)
CenterLongitude = openapi.Parameter('centerlongitude', openapi.IN_QUERY, description="Center Longitude", type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT)
Radius = openapi.Parameter('radius', openapi.IN_QUERY, description="Search Radius in meters", type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT)

@method_decorator(
    name='list', 
    decorator=swagger_auto_schema(
        operation_description="Retrieve all the cameras from the database within a circle defined by radius and point.",
        responses={
            400: 'if one of the parameters was not set or was not valid.',
            200: CameraSerializer(many=True)
        },
        manual_parameters=[
            CenterLatitude,
            CenterLongitude,
            Radius
            ]
))
class CameraRadiusSearchViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = CameraSerializer
    
    def get_queryset(self):
        centerlatitude  = self.request.query_params.get('centerlatitude', None)
        centerlongitude = self.request.query_params.get('centerlongitude', None)
        radius = self.request.query_params.get('radius', None)                                              
        if centerlatitude is None:
            raise serializers.ValidationError("Center Latitude cannot be none")
        if centerlongitude is None:
            raise serializers.ValidationError("Center Longitude cannot be none")
        if radius is None:
            raise serializers.ValidationError("Radius cannot be none")
        pnt = Point(float(centerlongitude), float(centerlatitude))
        queryset = Camera.objects.all().extra(where = ['ST_Distance_Sphere(Position, ST_PointFromText(%s, 4326)) <= %s'],params=[pnt.wkt,float(radius)])
        return queryset
    
    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list,many=True)
        return Response({'cameralist':serializer.data})
