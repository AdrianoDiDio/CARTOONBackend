from django.urls import include, path, re_path
from rest_framework import routers,permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'getcameralist', views.CameraListViewSet)
router.register(r'getnearbycameralist', views.CameraRadiusSearchViewSet, basename='getnearbycameralist')

schema_view = get_schema_view(
   openapi.Info(
      title="Cartoon Service API",
      default_version='v1',
      description="Utility Api to fetch a list of camera from server.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="95adriano@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path('^swagger/$', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 
